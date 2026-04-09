# 🔍 Advanced TCP Port Scanner

A professional Python-based port scanner designed to identify open and closed ports on a target system.  
This tool simulates real-world reconnaissance techniques used in cybersecurity and SOC environments.

---

## 🚀 Features

- 🔹 Multi-threaded scanning for faster performance  
- 🔹 CLI (Command-Line Interface) support  
- 🔹 Interactive mode for user-friendly execution  
- 🔹 Banner grabbing to identify running services  
- 🔹 Timeout handling for reliable scanning  
- 🔹 Exception handling for robustness  
- 🔹 Logs results to a file (`scan_results.txt`)  
- 🔹 Clean and structured output  

---

## 🧠 Key Concepts Used

- Socket Programming  
- Networking fundamentals (TCP connections, ports)  
- Multi-threading  
- Command-line argument parsing (`argparse`)  
- Error and exception handling  
- File handling in Python  

---

▶️ Usage


🔹 CLI Mode
python port_scanner.py <target_ip> <start_port> <end_port>

Example:

python port_scanner.py 127.0.0.1 20 100

With timeout:

python port_scanner.py 127.0.0.1 20 100 --timeout 1
🔹 Interactive Mode

Run without arguments:

python port_scanner.py

Then enter:

Target IP
Start Port
End Port

📂 Output

Results are displayed in the terminal with color-coded output
All scan results are saved automatically in:
scan_results.txt

📊 Sample Output

[OPEN] Port 22 | SSH-2.0-OpenSSH
[CLOSED] Port 80
[OPEN] Port 443 | No banner

🎯 Use Cases
Network reconnaissance
Security auditing
SOC Analyst practice
Learning TCP/IP and socket programming
Identifying exposed services

⚠️ Disclaimer

This tool is intended for educational and ethical use only.
Do not scan systems or networks without proper authorization.

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
