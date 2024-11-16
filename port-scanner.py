import socket
from datetime import datetime

def scan_port(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM
    socket.setdefaulttimeout(1)
    result = scanner.connect_ex((ip, port))
    scanner.close()
    return result == 0

def scan_ports(ip, start_port, end_port):
    print(f"Scanning target {ip}")
    start_time = datetime.now()
    for port in range(start_port, end_port + 1):
        if scan_port(ip, port):
            print(f"Port {port} is open")
    end_time = datetime.now()
    print(f"Scanning completed in: {end_time - start_time}")

if __name__ == "__main__":
    target = input("Enter the target IP address: ")
    port_range = input("Enter the range of ports to scan (e.g., 1-1000): ")
    start_port, end_port = map(int, port_range.split('-'))
    scan_ports(target, start_port, end_port)
    
