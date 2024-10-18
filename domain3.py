from googlesearch import search
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

def google_search(query, num_results=10):
    search_results = search(query, num_results=num_results)
    return search_results

def extract_domain(url):
    domain = urlparse(url).netloc
    return domain

def find_partners(company_name):
    query = f"{company_name} partners"
    search_results = google_search(query)
    partner_domains = set()

    for url in search_results:
        domain = extract_domain(url)
        partner_domains.add(domain)
    
    return partner_domains

def scrape_partners_from_wikipedia(company_name):
    url = f"https://en.wikipedia.org/wiki/{company_name.replace(' ', '_')}"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        partners_section = soup.find(id='Partners') or soup.find(id='Partnerships') or soup.find(id='Alliances')
        partner_domains = set()
        
        if partners_section:
            for li in partners_section.find_next('ul').find_all('li'):
                partner_name = li.get_text()
                partner_query = f"{partner_name} official site"
                partner_urls = google_search(partner_query, num_results=1)
                if partner_urls:
                    partner_domain = extract_domain(partner_urls[0])
                    partner_domains.add(partner_domain)
                    
        return partner_domains
    except Exception as e:
        print(f"Error scraping Wikipedia: {e}")
        return set()

def main():
    company_name = 'Tata Group'
    
    # Find partners from Google search
    google_partner_domains = find_partners(company_name)
    
    # Scrape partners from Wikipedia
    wikipedia_partner_domains = scrape_partners_from_wikipedia(company_name)
    
    # Combine results
    all_partner_domains = google_partner_domains.union(wikipedia_partner_domains)
    
    print(f"Associated domains for partners of {company_name}:")
    for domain in all_partner_domains:
        print(domain)

if __name__ == "__main__":
    main()
