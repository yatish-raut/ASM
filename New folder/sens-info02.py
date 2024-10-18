import requests
import dns.resolver

def enumerate_subdomains(domain):
    subdomains = []
    try:
        answers = dns.resolver.resolve(domain, 'A')
        for answer in answers:
            subdomains.append(answer.to_text())
    except dns.resolver.NoAnswer:
        pass
    except dns.resolver.NXDOMAIN:
        pass
    except Exception as e:
        print(f"Error enumerating subdomains: {e}")
    
    return subdomains

def test_sensitive_data_exposure(url):
    sensitive_endpoints = [
        '/api/users',
        '/api/orders',
        '/api/payment',
        '/api/account',
        '/admin',
        '/admin/logs',
        '/admin/users',
        '/login',
        '/reset-password',
        '/uploads',
        '/downloads',
        '/debug',
        '/error',
        '/third-party-api'
        # Add more endpoints as needed
    ]
    
    target_domain = url.split('//')[-1].split('/')[0]
    subdomains = enumerate_subdomains(target_domain)
    
    for subdomain in subdomains:
        for endpoint in sensitive_endpoints:
            endpoint_url = f"http://{subdomain}{endpoint}"
            try:
                response = requests.get(endpoint_url)
                
                # Check if sensitive information is present in the response
                if 'password' in response.text or 'credit_card' in response.text:
                    print(f"Sensitive Data Exposure found in endpoint: {endpoint_url}")
                else:
                    print(f"No Sensitive Data Exposure found in endpoint: {endpoint_url}")
            except requests.exceptions.RequestException as e:
                print(f"Error accessing {endpoint_url}: {e}")

def main():
    target_url = "https://youtube.com"
    test_sensitive_data_exposure(target_url)

if __name__ == "__main__":
    main()
