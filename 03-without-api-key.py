import os
import sys
import re
import json
import requests
import argparse
import tldextract
from colored import fg, attr

def searchDomainBuiltwith(domain, verbose, t_data):
    if verbose:
        print(f"{fg('green')}[+] calling BuiltWith targeting domain{attr(0)}")

    try:
        url = f'https://builtwith.com/relationships/{domain}'
        r = requests.get(url)
        r.raise_for_status()
    except requests.RequestException as e:
        print(f"{fg('red')}[-] error occurred: {e}{attr(0)}")
        return

    rgxp = r'("https://builtwith.com/relationships/[^"]+)'
    matches = re.findall(rgxp, r.text, re.IGNORECASE)

    for m in matches:
        if '/tag/' not in m:
            domain = m.replace('https://builtwith.com/relationships/', '').replace('"', '').lower()
            if domain not in t_data['domains']:
                t_data['domains'].append(domain)
                print(domain)

def searchDomainCrtsh(domain, verbose, t_data):
    if verbose:
        print(f"{fg('green')}[+] calling crt.sh targeting domain{attr(0)}")

    parse = tldextract.extract(domain)
    url = f'https://crt.sh/?q=%25{parse.domain}%25&output=json'
    if verbose:
        print(f"{fg('white')}[+] {url}{attr(0)}")

    try:
        r = requests.get(url)
        r.raise_for_status()
        t_json = r.json()
    except requests.RequestException as e:
        print(f"{fg('red')}[-] error occurred: {e}{attr(0)}")
        return

    for item in t_json:
        if 'common_name' in item:
            try:
                parse = tldextract.extract(item['common_name'])
                domain = f"{parse.domain}.{parse.suffix}".lower()
                if domain not in t_data['domains']:
                    t_data['domains'].append(domain)
                    print(domain)
            except Exception:
                continue

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", help="domain you already know (required)")
    parser.add_argument("-b", "--builtwith", help="use BuiltWith as a source", action="store_true")
    parser.add_argument("-s", "--source", help="list of sources separated by comma, available sources are: builtwith, crtsh (default=crtsh)", default="crtsh")
    parser.add_argument("-v", "--verbose", help="enable verbose mode, default off", action="store_true")
    args = parser.parse_args()

    t_data = {'domains': []}

    if args.verbose:
        verbose = True
    else:
        verbose = False

    if not args.domain:
        parser.error('Domain is required')

    domain = args.domain
    sources = args.source.split(',')

    if verbose:
        print(f"{fg('green')}[+] search for domain: {domain}{attr(0)}")

    if "crtsh" in sources:
        searchDomainCrtsh(domain, verbose, t_data)

    if "builtwith" in sources:
        searchDomainBuiltwith(domain, verbose, t_data)

if __name__ == "__main__":
    main()
