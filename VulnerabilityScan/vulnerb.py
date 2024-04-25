from . import nmap2,nmap5,vulnerabilty1

def main(ip,domain):
    nmap5.main(ip)
    nmap2.main(ip)
    vulnerabilty1.main(domain)