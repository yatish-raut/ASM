import requests

name = input("Enter name: ")

# Open and read the wordlist file
with open('sub.txt', 'r') as file:
    content = file.read()

subdomains = content.splitlines()

# Open and read the domain file
with open('domain.txt', 'r') as file2:
    content2 = file2.read()

domains = content2.splitlines()

for domain in domains:
    suffix = f"{name}.{domain}"
    for subdomain in subdomains:
        url1 = f"http://{subdomain}.{suffix}"
        url2 = f"https://{subdomain}.{suffix}"
        try:
            requests.get(url2)
            print(f"Discovered URL: {url2}")
            # requests.get(url1)
            # print(f"Discovered URL: {url1}")
        except requests.ConnectionError:
            pass

print('end')
