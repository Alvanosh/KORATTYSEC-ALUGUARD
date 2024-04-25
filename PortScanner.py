import socket
import concurrent.futures
import re
from urllib.parse import urlparse

def is_valid_ip(ip):
    # Regular expression to validate IP address
    ip_pattern = re.compile(
        r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}'
        r'([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'
    )
    return ip_pattern.match(ip) is not None

def get_target(ip_or_url):
    if is_valid_ip(ip_or_url):
        return ip_or_url
    else:
        parsed_url = urlparse(ip_or_url)
        return socket.gethostbyname(parsed_url.netloc)

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip, port))
            return port, 'open'
    except (socket.timeout, ConnectionRefusedError):
        return port, 'closed'
    except Exception as e:
        return port, 'error'

def scan(ip_or_url, start_port=1, end_port=1024, max_threads=100):
    ip = get_target(ip_or_url)
    open_ports = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(scan_port, ip, port) for port in range(start_port, end_port + 1)]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result[1] == 'open':
                open_ports.append(result[0])
    return open_ports

def main(url):
    target = url
    open_ports = scan(target)
    if open_ports:
        print("Open ports:")
        
        print(open_ports)
    else:
        print("No open ports found.")

