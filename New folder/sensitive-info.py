import requests

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
    
    for endpoint in sensitive_endpoints:
        endpoint_url = url + endpoint
        response = requests.get(endpoint_url)
        
        # Check if sensitive information is present in the response
        if 'password' in response.text or 'credit_card' in response.text:
            print(f"Sensitive Data Exposure found in endpoint: {endpoint_url}")
            #print(response.text)
        else:
            print(f"No Sensitive Data Exposure found in endpoint: {endpoint_url}")

def main():
    target_url = "https://data.vermont.gov"
    test_sensitive_data_exposure(target_url)

if __name__ == "__main__":
    main()
