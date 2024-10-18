import whois
from collections import defaultdict

def get_whois_info(domain_name):
    try:
        domain = whois.whois(domain_name)
        return domain
    except Exception as e:
        print(f"Error fetching WHOIS information for {domain_name}: {e}")
        return None

def find_domains_with_common_registrant(domain_names):
    registrant_map = defaultdict(list)
    
    for domain_name in domain_names:
        domain_info = get_whois_info(domain_name)
        if domain_info and domain_info.registrar:
            registrant = domain_info.registrar.lower()  # Normalize to lower case for case insensitivity
            registrant_map[registrant].append(domain_name)
    
    common_domains = []
    for registrant, domains in registrant_map.items():
        if len(domains) > 1:
            common_domains.extend(domains)
    
    return common_domains

def main():
    domain_names = [
        'tata.com',
        'tataaig.org',
        'example.net'
        # Add more domains here as needed
    ]
    
    common_domains = find_domains_with_common_registrant(domain_names)
    
    if common_domains:
        print(f"Domains with common registrant:")
        for domain in common_domains:
            print(domain)
    else:
        print("No domains found with common registrant.")

if __name__ == "__main__":
    main()
