from . import PortScanner, Ipget , IpGeolocation,Whois

def main(url,ip,domain):
    
    PortScanner.main(url)
  
    
    IpGeolocation.main(ip)
    Whois.main(domain)

