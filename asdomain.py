import requests
from bs4 import BeautifulSoup
from googlesearch import search

def google_search(query):
    search_results = []
    for url in search(query, num_results=1):
        search_results.append(url)
    return search_results

def scrape_associated_domains(urls, keywords):
    associated_domains = set()
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            links = [a['href'] for a in soup.find_all('a', href=True)]
            for link in links:
                if any(keyword.lower() in link.lower() for keyword in keywords):
                    associated_domains.add(link)
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
    return associated_domains

def main():
    company_name = 'Tata'
    associated_company_name = 'Starbucks'
    
    # Google search for partnerships between the companies
    query = f"{company_name} {associated_company_name} partnership"
    search_results = google_search(query)
    
    # Keywords to look for in links
    keywords = [company_name, associated_company_name]
    
    # Scrape associated domains from the search results
    associated_domains = scrape_associated_domains(search_results, keywords)
    
    print(f"Associated domains found for {company_name} and {associated_company_name}:")
    for domain in associated_domains:
        print(domain)

if __name__ == "__main__":
    main()
