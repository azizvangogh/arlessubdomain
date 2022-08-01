import requests

domain = input("Enter domain (Example google.com) : ")

pp = input("Enter path (Example /subdomains) : ")

file = open(pp)

content = file.read()

subdomains = content.splitlines()


finding_subdomains = []
for subdomain in subdomains:
    url = f'https://{subdomain}.{domain}'
    try:
        r = requests.get(url)
        if r.status_code == 200:
            finding_subdomains.append(subdomain)
    except:
        pass

    else:
        print("Discovered subdomain : ", url)
        print("\n")
        finding_subdomains.append(subdomain)

with open ("subdomains.txt", "w") as f:
    for subdomain in finding_subdomains:
        f.write(subdomain)
        f.write("\n")
        print("[+] Subdomain saved in subdomains.txt")
        print("[+] Done")
        print("[+] Check subdomains.txt")
        print("[+] Thank you for using subfinder")
        print("[+] Created by : @azizovskii")
        print("[+] Github : https://github.com/azizvangogh/arlessubfinder")