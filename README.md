# CODTECH-Task2
Vulnerability scanner
Overview
The Simple Vulnerability Scanner is a lightweight tool designed to scan a target network or website for common security vulnerabilities such as open ports, outdated software versions, and simple misconfigurations.

Features
Port Scanning: Identifies open ports in the range of 1-1024.
Server Version Identification: Retrieves the server version from HTTP response headers.
Misconfiguration Detection: Checks for common issues like exposed admin pages and directory listings.
Requirements
Python 3.x
Additional Python Packages:
requests
beautifulsoup4
Installation
Install Python 3.x: Ensure Python 3.x is installed on your system.

Install Required Packages:

bash
Copy code
pip install requests beautifulsoup4
Usage
Clone the Repository.
Run the Vulnerability Scanner:

bash
Copy code
python simple_vulnerability_scanner.py
Configure Target:

In the script, set the target IP and URL:
python
Copy code
target_ip = "127.0.0.1"  # Replace with the target IP address
target_url = "http://localhost"  # Replace with the target URL
This will scan the localhost by default. Modify these values to scan a different target.
Example Output
bash
Copy code
Starting vulnerability scan...
Scanning for open ports on 127.0.0.1...
Port 80: Open
Port 443: Open
Checking server version for http://localhost...
Server version: Apache/2.4.41 (Ubuntu)
Checking for common misconfigurations at http://localhost...
No common misconfigurations found.
Vulnerability scan completed.
Limitations
This is a basic vulnerability scanner and does not replace professional security assessment tools.
It scans only a limited range of ports and performs simple checks.
