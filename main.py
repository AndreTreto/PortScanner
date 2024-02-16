import socket

found_ports = []

def get_host(host):
    ip = socket.gethostbyname(host)
    print(ip)
    return ip


def scan_ports(target_ip, port):
    try:

        sock = socket.socket()
        sock.settimeout(.1)
        sock.connect((target_ip, port))
        banner = sock.recv(1024)
        print(f"Port open at {port} with target ip at {target_ip}, with {banner}")
        found_ports.append(port)
    except:
        pass
    finally:
        sock.close()

def scanoverview(array):
  port_names = {
    7: "ECHO",
    19: "CHARGEN",
    20: "FTP-DATA",
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    42: "WINS REPLICATION",
    43: "WHOIS",
    49: "TACACS",
    53: "DNS",
    67: "DHCP",
    68: "DHCPV6",
    69: "TFTP",
    70: "GOPHER",
    79: "FINGER",
    80: "HTTP",
    88: "KERBEROS",
    102: "MS-NTP",
    109: "POP2",
    110: "POP3",
    111: "RPC",
    113: "IDENT",
    115: "SFTP",
    117: "UUCP",
    119: "NNTP",
    123: "NTP",
    135: "RPC-EPMAP",
    137: "NETBIOS-NS",
    138: "NETBIOS-DGM",
    139: "NETBIOS-SS",
    143: "IMAP4",
    161: "SNMP",
    162: "SNMPTRAP",
    163: "SNMPTRAP-TRAP",
    179: "BGP",
    194: "IRC",
    201: "APPLETALK",
    264: "BGMP",
    318: "TSP",
    326: "LDAP",
    381: "HP-OPENVIEW",
    389: "LDAP",
    427: "SLP",
    443: "HTTPS",
    3306: "MYSQL",
    8080: "HTTP PROXY",
    8443: "HTTPS PROXY",
    
  }
  for port in array:
    if port in port_names:
        print(f"PORT {port}: {port_names[port]}")

def encryption(array):
    if 443 in array:
        print("ENCRYPTION: TRUE")
    else:
        print("ENCRYPTION: FALSE")

website = input("Enter website to scan: ")
get_host(website)

for port in range(0, 8444):
    scan_ports(website, port)

print("Scan complete")
print("  OVERVIEW (0-8444): ")
print("--------------")
scanoverview(found_ports)
encryption(found_ports)
print("--------------")




