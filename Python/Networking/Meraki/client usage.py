import requests
import json

url = "https://dashboard.meraki.com/api/v0/organizations"

headers = {
    'X-Cisco-Meraki-API-Key': "9103a4d27fc670d50f63f9d6047c0de121f475f1",
}

response = requests.get(url, headers=headers).json()

#print(json.dumps(response, indent=2, sort_keys=True))

for response_org in response:
    if response_org['name'] == 'DevNet Sandbox':
        orgId = response_org['id']

net_url = f'{url}/{orgId}/networks'

networks = requests.get(net_url, headers=headers).json()
# print(networks)
for network in networks:
    if network['name'] == 'DNSMB3-axxxxxagmail.com':
        netId = network['id']

client_url = f'https://dashboard.meraki.com/api/v0/networks/{netId}/clients'
clients = requests.get(client_url, headers=headers).json()
#print(json.dumps(clients, indent=2, sort_keys=True))
for client in clients:
    if client['id'] == 'k60f829':
        clientid = client['id']
traffic_url = f"https://dashboard.meraki.com/api/v0/networks/{netId}/clients/{clientid}/usageHistory"
historys = requests.get(traffic_url, headers=headers).json()
print(json.dumps(historys, indent=2, sort_keys=True))
