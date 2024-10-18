import whois

def get_whois_info(domain_name):
    try:
        domain = whois.whois(domain_name)
        return domain
    except Exception as e:
        print(f"Error fetching WHOIS information for {domain_name}: {e}")
        return None

def main():
    domain_name = 'chatgpt.com'  # Replace with the domain name you want to query
    domain_info = get_whois_info(domain_name)
    
    if domain_info:
        print(f"WHOIS information for {domain_name}:")
        print(domain_info)
    else:
        print(f"Failed to fetch WHOIS information for {domain_name}")
    print("default")

if __name__ == "__main__":
    main()