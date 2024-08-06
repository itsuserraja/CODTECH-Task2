import socket
import requests
from bs4 import BeautifulSoup

def scan_open_ports(target_ip):
    print(f"Scanning for open ports on {target_ip}...")
    open_ports = []
    for port in range(1, 1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
            print(f"Port {port}: Open")
        sock.close()
    return open_ports

def check_server_version(target_url):
    print(f"Checking server version for {target_url}...")
    try:
        response = requests.head(target_url)
        server = response.headers.get('Server', 'Unknown')
        print(f"Server version: {server}")
        return server
    except requests.RequestException as e:
        print(f"Error checking server version: {e}")
        return None

def check_common_misconfigurations(target_url):
    print(f"Checking for common misconfigurations at {target_url}...")
    misconfigurations = []
    try:
        response = requests.get(target_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        if soup.title and 'admin' in soup.title.string.lower():
            misconfigurations.append("Potential exposed admin page found.")

        if "Index of /" in response.text:
            misconfigurations.append("Directory listing is enabled.")


    except requests.RequestException as e:
        print(f"Error checking misconfigurations: {e}")

    if misconfigurations:
        for issue in misconfigurations:
            print(issue)
    else:
        print("No common misconfigurations found.")

    return misconfigurations

def run_vulnerability_scan(target_ip, target_url):
    print("Starting vulnerability scan...")

    scan_open_ports(target_ip)

    check_server_version(target_url)

    check_common_misconfigurations(target_url)

    print("Vulnerability scan completed.")

if __name__ == "__main__":

    target_ip = "127.0.0.1" 
    target_url = "http://localhost"  

    run_vulnerability_scan(target_ip, target_url)
