import requests
from colored import fg, attr

def check_security_headers(url):
    response = requests.get(url)
    headers = response.headers

    # Define security headers to check
    security_headers = [
        ('X-Frame-Options', 'X-Frame-Options header missing - vulnerable to clickjacking', fg('red')),
        ('Content-Security-Policy', 'Content-Security-Policy header missing - vulnerable to XSS', fg('red')),
        ('Strict-Transport-Security', 'Strict-Transport-Security header missing - not enforcing HTTPS', fg('yellow')),
        ('X-XSS-Protection', 'X-XSS-Protection header missing - vulnerable to XSS', fg('red')),
        ('X-Content-Type-Options', 'X-Content-Type-Options header missing - vulnerable to MIME-sniffing attacks', fg('red')),
        ('Referrer-Policy', 'Referrer-Policy header missing - may leak sensitive information', fg('yellow')),
        ('Feature-Policy', 'Feature-Policy header missing - allows all features by default', fg('yellow')),
        ('X-Permitted-Cross-Domain-Policies', 'X-Permitted-Cross-Domain-Policies header missing - may allow cross-domain policy files', fg('yellow')),
        ('Expect-CT', 'Expect-CT header missing - vulnerable to certificate transparency policy violations', fg('red')),
        ('X-Download-Options', 'X-Download-Options header missing - allows automatic file downloads without user interaction', fg('yellow')),
        ('Permissions-Policy', 'Permissions-Policy header missing - controls which features and APIs can be used by the site', fg('yellow')),
        ('Content-Security-Policy-Report-Only', 'Content-Security-Policy-Report-Only header missing - report-only mode for CSP allows testing without blocking', fg('yellow')),
        ('X-Content-Security-Policy', 'X-Content-Security-Policy header missing - legacy version of Content-Security-Policy', fg('yellow')),
        ('X-WebKit-CSP', 'X-WebKit-CSP header missing - legacy version of Content-Security-Policy for WebKit browsers', fg('yellow'))
    ]

    # Check each header in the security_headers array
    for header_name, message, color_code in security_headers:
        if header_name not in headers:
            colored_message = f"{color_code}{message}{attr('reset')}"
            print(colored_message)

# Example usage
domain = input("Enter your desired domain \n")

check_security_headers(domain)
