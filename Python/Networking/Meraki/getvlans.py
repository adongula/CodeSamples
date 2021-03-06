import requests
import json


url = "https://dashboard.meraki.com/api/v0/organizations"

headers = {
    'X-Cisco-Meraki-API-Key': '9103a4d27fc670d50f63f9d6047c0de121f475f1,
}

response = requests.get(url, headers=headers).json()

for response_org in response:
    if response_org['name'] == 'CBT Nuggets':
        orgId = response_org['id']

net_url = f'{url}/{orgId}/networks'

networks = requests.get(net_url, headers=headers).json()
print(json.dumps(networks, indent=2, sort_keys=True))

vlan_url = f'https://dashboard.meraki.com/api/v0/networks/{netId}/vlans'
vlans = requests.get(vlan_url, headers=headers).json()
print(json.dumps(vlans, indent=2, sort_keys=True))
