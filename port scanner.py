import socket

def custom_port_scanner(target):
    print(f"--- Starting Scan on {target} ---")

    try:
        target_ip = socket.gethostbyname(target)
        print(f"Target IP resolved: {target_ip}\n")
    except socket.gaierror:
        print("Error: Could not resolve hostname.")
        return

    ports_to_scan = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        135: "MSRPC",
        139: "NetBIOS",
        143: "IMAP",
        161: "SNMP",
        389: "LDAP",
        443: "HTTPS",
        445: "SMB",
        587: "SMTP Submission",
        636: "LDAPS",
        993: "IMAPS",
        995: "POP3S",
        1433: "MSSQL",
        1521: "Oracle",
        2049: "NFS",
        2375: "Docker",
        3306: "MySQL",
        3389: "RDP",
        5432: "PostgreSQL",
        5985: "WinRM HTTP",
        5986: "WinRM HTTPS",
        6379: "Redis",
        8080: "HTTP Proxy",
        8443: "HTTPS Alternate"
    }

    for port, service in ports_to_scan.items():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target_ip, port))

        if result == 0:
            print(f"[+] Port {port} is OPEN ({service})")
        else:
            print(f"[-] Port {port} is closed")

        s.close()

target = input("Enter an IP address or website: ")
custom_port_scanner(target)