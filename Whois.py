import whois
from datetime import datetime

def get_whois_info(domain_name):
    try:
        w = whois.whois(domain_name)

        return w
    except Exception as e:
        return f"Error: {e}"

def print_basic_info(whois_info):
    if not whois_info:
        print("No WHOIS information found.")
        return

    print("Domain Name:", whois_info.domain_name)
    print("Registrar:", whois_info.registrar)
    print("Creation Date:", whois_info.creation_date)
    print("Expiration Date:", whois_info.expiration_date)
    print("Last Updated Date:", whois_info.last_updated)
    print("Registrant Name : " , whois_info.name)
    print("Organization : " , whois_info.org)
    print("Address : " , whois_info.address)
    print("Registrant Name : " , whois_info.name)
    print("Emails")
    for i in whois_info.emails:
        print(f"-     {i}")

def print_extended_info(whois_info):
    if not whois_info:
        print("No WHOIS information found.")
        return

    print("Name Servers:")
    for ns in whois_info.name_servers:
        print("-", ns)

    print("\nRegistrant Information:")
    if whois_info.registrant_name:
        print("Name:", whois_info.registrant_name)
    if whois_info.registrant_organization:
        print("Organization:", whois_info.registrant_organization)
    if whois_info.registrant_email:
        print("Email:", whois_info.registrant_email)
    if whois_info.registrant_phone:
        print("Phone:", whois_info.registrant_phone)

def print_all_info(whois_info):
    if not whois_info:
        print("No WHOIS information found.")
        return

    print("Domain Name:", whois_info.domain_name)
    print("Registrar:", whois_info.registrar)
    print("Creation Date:", whois_info.creation_date)
    print("Expiration Date:", whois_info.expiration_date)
    print("Last Updated Date:", whois_info.last_updated)
    

    print("\nName Servers:")
    for ns in whois_info.name_servers:
        print("-", ns)

    print("\nRegistrant Information:")
    if whois_info.registrant_name:
        print("Name:", whois_info.nam)
    if whois_info.registrant_organization:
        print("Organization:", whois_info.registrant_organization)
    if whois_info.registrant_email:
        print("Email:", whois_info.registrant_email)
    if whois_info.registrant_phone:
        print("Phone:", whois_info.registrant_phone)

def main(domain_name):
    
    whois_info = get_whois_info(domain_name)

    if isinstance(whois_info, str):
        print(whois_info)
        return
    print(whois_info)

    print("\nBasic Information:")
    print_basic_info(whois_info)


