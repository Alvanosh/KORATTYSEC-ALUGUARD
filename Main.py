from Osint import Osint
from Osint import Ipget
from VulnerabilityScan import vulnerb
import custom_wordlitsmaker
import wireshark
import pyfiglet

from colorama import Fore
styled_text=pyfiglet.figlet_format('KORATTYSEC ALUGUARD',font= 'doom')
print(Fore.RED + styled_text)
a = input("Enter the 1 for Osint\n2 for Vulnerablibility Check\n3 for password Word List generation\n4 for packet sniffer")
if a == "3":
    custom_wordlitsmaker.main()
elif a == "4":
        wireshark.main()    
else:
    url = input(("Input Url You want to Search"))

    [ip,domain] = Ipget.main(url)
    if a == "1":
        print(1)
        Osint.main(url,ip,domain)
    if a== "2":
        print(2)
        vulnerb.main(ip,domain)
   