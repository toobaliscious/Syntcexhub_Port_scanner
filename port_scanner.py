import socket
import threading
import argparse
from datetime import datetime
from colorama import Fore, init
import os

# Initialize colorama
init(autoreset=True)

# -------------------------------
# Global storage
# -------------------------------
open_ports = []
closed_ports = []

lock = threading.Lock()

# -------------------------------
# Banner grabbing
# -------------------------------
def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        banner = s.recv(1024).decode(errors="ignore").strip()
        s.close()
        return banner if banner else "No banner"
    except:
        return "No banner"

# -------------------------------
# Scan function
# -------------------------------
def scan_port(ip, port, timeout):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)

        result = s.connect_ex((ip, port))

        if result == 0:
            banner = grab_banner(ip, port)
            print(Fore.GREEN + f"[OPEN] Port {port} | {banner}")
            with lock:
                open_ports.append((port, banner))
        else:
            print(Fore.RED + f"[CLOSED] Port {port}")
            with lock:
                closed_ports.append(port)

        s.close()

    except Exception as e:
        print(Fore.YELLOW + f"[ERROR] Port {port}: {e}")

# -------------------------------
# Argument parser
# -------------------------------
parser = argparse.ArgumentParser(description="Advanced Port Scanner")

parser.add_argument("target", nargs="?", help="Target IP")
parser.add_argument("start_port", nargs="?", type=int, help="Start port")
parser.add_argument("end_port", nargs="?", type=int, help="End port")
parser.add_argument("--timeout", type=float, default=1, help="Timeout per port")

args = parser.parse_args()

# -------------------------------
# Input mode
# -------------------------------
if not args.target:
    print(Fore.CYAN + "\n=== INTERACTIVE MODE ===")
    target = input("Enter target IP: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    timeout = 1
else:
    target = args.target
    start_port = args.start_port
    end_port = args.end_port
    timeout = args.timeout

# -------------------------------
# Start scanning
# -------------------------------
print(Fore.CYAN + "\n===== SCANNING STARTED =====")
print(f"Target: {target}")
print(f"Ports: {start_port} - {end_port}\n")

start_time = datetime.now()

threads = []

for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(target, port, timeout))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = datetime.now()

# -------------------------------
# Summary
# -------------------------------
print(Fore.CYAN + "\n===== SCAN COMPLETE =====")
print(f"Time: {start_time} - {end_time}")
print(Fore.GREEN + f"Open Ports: {len(open_ports)}")
print(Fore.RED + f"Closed Ports: {len(closed_ports)}")

# -------------------------------
# Save results to file
# -------------------------------
filepath = r"C:\Syncexhub\scan_results.txt"

with open(filepath, "w", encoding="utf-8") as file:
    file.write("===== PORT SCAN REPORT =====\n\n")
    file.write(f"Target: {target}\n")
    file.write(f"Scan Time: {start_time} - {end_time}\n\n")

    file.write("Open Ports:\n")
    for port, banner in open_ports:
        file.write(f"{port} - {banner}\n")

    file.write("\nClosed Ports:\n")
    for port in closed_ports:
        file.write(f"{port}\n")

print(Fore.CYAN + f"\nResults successfully saved to: {filepath}")
