import socket 
from urllib.parse import urlparse




def main(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    ip = socket.gethostbyname(domain)


    print("Ip address :  " + ip)
    print("Domain : " + domain)
    return ip,domain


#display the IP
