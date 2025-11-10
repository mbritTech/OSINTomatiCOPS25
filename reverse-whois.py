import requests
import json
from config import WHOISXMLAPI_APIKEY as API_KEY # Reemplaza con tu clave real de WhoisXML en el fichero config

name = "NOMBRE A INVESTIGAR"

url = "https://reverse-whois.whoisxmlapi.com/api/v2"
params = {
    "apiKey": API_KEY,
    "searchType": "current",
    "mode": "purchase",
    "punycode": True,
    "basicSearchTerms": {
        "include": [
            name
        ]
    }
}

resp = requests.post(url, json=params)

file_to_save_domains = 'ck-domains.txt'

if resp.status_code == 200:
    data = resp.json()
    domains_list = data['domainsList']

    print(f"Se han encontrado {data['domainsCount']} dominios relacionados con {name}:")
    print(json.dumps(domains_list, indent=4, ensure_ascii=False))

    print("Se va a crear un fichero con dominios a comprobar")
    with open(file_to_save_domains, 'w') as domain_f:
        for domain in domains_list:
            domain_f.write(domain+'\n')
    print(f"Creación del fichero '{file_to_save_domains}' OK")

else:
    print("Error:", resp.status_code, resp.text)
