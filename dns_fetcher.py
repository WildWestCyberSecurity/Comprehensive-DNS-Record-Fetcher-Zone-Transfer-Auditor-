import dns.resolver
import dns.query
import dns.zone
import pandas as pd
from tabulate import tabulate
import argparse

def get_dns_records(domain):
    records = {'A': [], 'AAAA': [], 'CNAME': [], 'MX': [], 'TXT': [], 'NS': [], 'SRV': [], 'Zone Transfer': []}
    
    try:
        answers = dns.resolver.resolve(domain, 'A')
        records['A'] = [answer.to_text() for answer in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
        pass

    try:
        answers = dns.resolver.resolve(domain, 'AAAA')
        records['AAAA'] = [answer.to_text() for answer in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
        pass

    try:
        answers = dns.resolver.resolve(domain, 'CNAME')
        records['CNAME'] = [answer.to_text() for answer in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
        pass

    try:
        answers = dns.resolver.resolve(domain, 'MX')
        records['MX'] = [answer.to_text() for answer in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
        pass

    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        records['TXT'] = [answer.to_text() for answer in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
        pass

    try:
        answers = dns.resolver.resolve(domain, 'NS')
        records['NS'] = [answer.to_text() for answer in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
        pass

    try:
        answers = dns.resolver.resolve(domain, 'SRV')
        records['SRV'] = [answer.to_text() for answer in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
        pass
    
    # Attempt zone transfer for each NS record
    ns_servers = records['NS']
    for ns_server in ns_servers:
        try:
            zone = dns.zone.from_xfr(dns.query.xfr(ns_server, domain))
            for name, node in zone.nodes.items():
                records['Zone Transfer'].append(str(name) + " " + str(node))
        except Exception as e:
            records['Zone Transfer'].append(f"Failed zone transfer attempt on {ns_server}: {e}")
    
    return records

def main():
    parser = argparse.ArgumentParser(description="Extract DNS records for a list of domains.")
    parser.add_argument('-d', '--domains', required=True, help="Path to the domains.txt file")
    args = parser.parse_args()

    with open(args.domains) as f:
        domains = f.read().splitlines()

    all_records = []

    for domain in domains:
        print(f"Fetching DNS records for: {domain}")
        records = get_dns_records(domain)
        for record_type, values in records.items():
            for value in values:
                all_records.append({
                    'Domain': domain,
                    'Record Type': record_type,
                    'Value': value
                })

    df = pd.DataFrame(all_records)

    # Print to console in a nice readable format
    print(tabulate(df, headers='keys', tablefmt='grid'))

    # Save to CSV
    df.to_csv('dns_records.csv', index=False)
    print("\nDNS records saved to dns_records.csv")

if __name__ == "__main__":
    main()
