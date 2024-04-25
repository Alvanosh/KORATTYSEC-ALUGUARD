import socket
import threading
from queue import Queue
import requests
import ssl
import whois

# Define the number of threads to use
NUM_THREADS = 50
# Define the timeout for socket connections
SOCKET_TIMEOUT = 1
# Define a list of common directories to fuzz
COMMON_DIRECTORIES = ["admin", "login", "images", "css", "js"]

def port_scan(ip_address, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt
        sock.settimeout(SOCKET_TIMEOUT)
        # Attempt to connect to the IP address and port
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            print(f"Port {port} is open")
        # Close the socket
        sock.close()
    except KeyboardInterrupt:
        print("Scan aborted by user")
    except socket.error:
        print("Could not connect to server")

def brute_force_login(ip_address, username, password):
    try:
        # Perform login attempt with username and password
        response = requests.post(f"http://{ip_address}/login", data={"username": username, "password": password})
        if response.status_code == 200:
            print("Login successful with:")
            print(f"Username: {username}")
            print(f"Password: {password}")
        else:
            print("Brute force login failed")
    except requests.RequestException:
        print("Error during brute force login attempt")

def ssl_check(ip_address):
    try:
        context = ssl.create_default_context()
        # Check port 443 for SSL support
        with socket.create_connection((ip_address, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=ip_address) as ssock:
                print("SSL is supported on port 443")
    except ssl.SSLError:
        print("SSL is not supported on port 443")

    try:
        # Check port 80 for SSL support
        context = ssl.create_default_context()
        with socket.create_connection((ip_address, 80)) as sock:
            with context.wrap_socket(sock, server_hostname=ip_address) as ssock:
                print("SSL is supported on port 80")
    except ssl.SSLError:
        print("SSL is not supported on port 80")

def web_server_detection(ip_address):
    try:
        response = requests.get(f"http://{ip_address}")
        print("Web Server Information:")
        print(f"Status Code: {response.status_code}")
        print(f"Server Header: {response.headers.get('Server', 'Not Found')}")
    except requests.RequestException:
        print("Error retrieving web server information")

def cms_detection(ip_address):
    # Placeholder for CMS detection
    print("CMS Detection: Not implemented yet")

def cloudflare_detection(ip_address):
    try:
        response = requests.get(f"http://{ip_address}")
        if 'Server' in response.headers and 'cloudflare' in response.headers['Server'].lower():
            print("Cloudflare Detected: True")
        else:
            print("Cloudflare Detected: False")
    except requests.RequestException:
        print("Error retrieving web server information")

def whois_lookup(domain):
    try:
        domain_info = whois.whois(domain)
        print("WHOIS Lookup Information:")
        print(domain_info)
    except Exception as e:
        print(f"Error during WHOIS lookup: {e}")

def worker(ip_address,port_queue):
    while True:
        
        # Get the port number from the queue
        port = port_queue.get()
        # Perform the port scan
        port_scan(ip_address, port)
        # Mark the task as done
        port_queue.task_done()

def main(domain):
    
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"Scanning {domain} ({ip_address})...\n")

        start_port = int(input("Enter the start port number: "))
        end_port = int(input("Enter the end port number: "))

        # Create a queue to hold the port numbers
        port_queue = Queue()

        # Add ports to the queue
        for port in range(start_port, end_port + 1):
            port_queue.put(port)

        # Create and start worker threads
        for _ in range(NUM_THREADS):
            t = threading.Thread(target=worker, args=(ip_address,port_queue))
            t.daemon = True
            t.start()

        # Wait for all tasks in the queue to be processed
        port_queue.join()

        # Perform additional scanning tasks
        brute_force_login(ip_address, "admin", "password")
        ssl_check(ip_address)
        web_server_detection(ip_address)
        cms_detection(ip_address)
        cloudflare_detection(ip_address)
        whois_lookup(domain)

    except socket.gaierror:
        print("Invalid domain name or unable to resolve the domain.")
