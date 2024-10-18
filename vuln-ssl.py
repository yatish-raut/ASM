import ssl
import socket

def check_ssl_tls_configuration(domain):
    context = ssl.create_default_context()
    try:
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                print(f"SSL/TLS Version: {ssock.version()}")
                print(f"Cipher: {ssock.cipher()}")
    except Exception as e:
        print(f"Error checking SSL/TLS configuration: {e}")

# Example usage:
domain = 'youtube.com'
check_ssl_tls_configuration(domain)
