import subprocess

def run_nmap_scan(target, options):
    nmap_command = ['nmap', target] + options.split()
    try:
        result = subprocess.run(nmap_command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error executing Nmap command: {e.stderr}"

def main(target):

    options = input("Enter Nmap options (e.g., -sL -sn -Pn -PS -PA -PU -PR -n): ")

    print("\nRunning Nmap scan:")
    scan_output = run_nmap_scan(target, options)
    print(scan_output)
