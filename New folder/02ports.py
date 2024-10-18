import socket

target_host = "data.vermont.gov"
target_ports = [21, 22, 80, 443]

common_ports = [
    (21, "FTP"),
    (22, "SSH"),
    (25, "SMTP"),
    (53, "DNS"),
    (80, "HTTP"),
    (110, "POP3"),
    (143, "IMAP"),
    (443, "HTTPS"),
    (3306, "MySQL"),
    (3389, "RDP"),
    (8080, "HTTP (alternate)"),
    (123, "NTP"),
    (137, "NetBIOS"),
    (138, "NetBIOS"),
    (139, "NetBIOS"),
    (161, "SNMP")
]

for port,name in common_ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target_host, port))
    if result == 0:
        print(f"Port {port}: Open    Name: {name}")
    sock.close()
