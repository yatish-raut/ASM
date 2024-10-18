import whois

def get_whois_info(domain):
    try:
        whois_info = whois.whois(domain)
        return whois_info
    except Exception as e:
        print(f"Error fetching WHOIS information for {domain}: {str(e)}")
        return None

def find_common_fields(domain1, domain2):
    info1 = get_whois_info(domain1)
    info2 = get_whois_info(domain2)

    if info1 and info2:
        print(f"Comparing WHOIS information for domains '{domain1}' and '{domain2}':")
        if info1 == info2:
            print("WHOIS information is identical for both domains.")
        else:
            print("WHOIS information differs for the following fields:")
            for key in info1.keys():
                if key in info2.keys() and info1[key] != info2[key]:
                    print(f"- {key}:")
                    print(f"   {domain1}: {info1[key]}")
                    print(f"   {domain2}: {info2[key]}")

        print(f"Common WHOIS fields for domains '{domain1}' and '{domain2}':")
        common_fields = set(info1.keys()) & set(info2.keys())
        if common_fields:
            for field in common_fields:
                print(f"- {field}")
        else:
            print("No common WHOIS fields found.")
    else:
        print("Unable to fetch WHOIS information for both domains.")

# Example usage:
domain1 = "tataaig.com"
domain2 = "tataaiginsurance.in"

find_common_fields(domain1, domain2)
