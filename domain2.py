from googlesearch import search
from urllib.parse import urlparse

def get_domains(query, num_results=10):
    search_results = search(query, num_results=num_results)
    domains = set()
    
    for url in search_results:
        domain = urlparse(url).netloc
        domains.add(domain)
    
    return domains

def main():
    company_name = 'Tata'
    associated_company_name = 'Starbucks'
    
    # Google search for partnerships between the companies
    query = f"{company_name} {associated_company_name} partnership"
    
    # Get domain names from search results
    domains = get_domains(query)
    
    print(f"Associated domains found for {company_name} and {associated_company_name}:")
    for domain in domains:
        print(domain)

if __name__ == "__main__":
    main()
