from googlesearch import search
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
import socket

def google_search(query, num_results=10):
    return [url for url in search(query, num_results=num_results)]

def extract_domains_from_search_results(query, num_results=10):
    search_results = google_search(query, num_results=num_results)
    domains = set()
    for url in search_results:
        domain = urlparse(url).netloc
        domains.add(domain)
    return domains

def resolve_domain(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.error as e:
        print(f"Error resolving domain {domain}: {e}")
        return None

def main():
    # company_name = 'Tata Group'
    company_name = input('Enter name: ')
    
    # Search for associated domains
    query = f"{company_name} associated domains"
    associated_domains = extract_domains_from_search_results(query)
    
    print(f"Associated domains of {company_name}:")
    for domain in associated_domains:
        print(domain)
    
    print("\nResolving IP addresses...")
    for domain in associated_domains:
        ip_address = resolve_domain(domain)
        if ip_address:
            print(f"Domain: {domain} \t IP Address: {ip_address}")
        else:
            print(f"Failed to resolve IP address for domain: {domain}")

if __name__ == "__main__":
    main()
