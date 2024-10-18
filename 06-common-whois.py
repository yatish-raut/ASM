import whois

def get_whois_info(domain):
    try:
        whois_info = whois.whois(domain)
        return whois_info
    except Exception as e:
        print(f"Error fetching WHOIS information for {domain}: {str(e)}")
        return None

def compare_common_fields(domain1, domain2):
    info1 = get_whois_info(domain1)
    info2 = get_whois_info(domain2)

    if info1 and info2:
        print(f"Comparing WHOIS information for domains '{domain1}' and '{domain2}':")
        common_fields = set(info1.keys()) & set(info2.keys())
        if common_fields:
            for field in common_fields:
                value1 = info1[field]
                value2 = info2[field]
                if value1 == value2:
                    print(f"- {field}: Same value for both domains - {value1}")
                else:
                    print(f"- {field}:")
                    print(f"   {domain1}: {value1}")
                    print(f"   {domain2}: {value2}")
                print()  # Empty line for separation
        else:
            print("No common WHOIS fields found.")
    else:
        print("Unable to fetch WHOIS information for both domains.")

# Example usage:
domain1 = "tata.com"
domain2 = "tatacapital.com"

compare_common_fields(domain1, domain2)
