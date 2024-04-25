import subprocess

def run_nmap_scan(target, options):
    nmap_command = ['nmap', target] + options.split()
    result = subprocess.run(nmap_command, capture_output=True, text=True)
    return result.stdout

def main(target):
    
    options = input("Enter Nmap options (e.g., -sS -A -p1-65535): ")

    print("\nRunning Nmap scan:")
    print(run_nmap_scan(target, options))
