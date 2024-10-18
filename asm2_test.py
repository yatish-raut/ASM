import requests

name = input("Enter name: ")
file = open('wordlist.txt','r')
content = file.read()

subdomains = content.splitlines()

file2 = open('domain.txt','r')
content2 = file.read()

domains = content2.splitlines()


for domain in domains:
	suffix = f"{name}.{domain}"
	for subdomain in subdomains:
		url1 = f"http://{subdomain}.{suffix}"
		url2 = f"https://{subdomain}.{suffix}"
		try:
			# requests.get(url1)
			# print(f"Discovered URL: {url1}")
			requests.get(url2)
			print(f"Discovered URL: {url2}")
			requests.get(url1)
			print(f"Discovered URL: {url1}")
		except requests.ConnectionError:
			pass

print('end')