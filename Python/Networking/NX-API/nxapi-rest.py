import requests
from pprint import pprint

url = "https://10.10.20.58/api/aaaLogin.json"

payload = "{\n    \"aaaUser\":{\n        \"attributes\":{\n            \"name\":\"admin\",\n            \"pwd\":\"Cisco123\"\n        }\n    }\n}"
headers = {
    'Content-Type': 'application/json',
}

response = requests.post(url, headers=headers,
                         data=payload, verify=False).json()

# Extracting out the token from response
token = response['imdata'][0]['aaaLogin']['attributes']['token']

# Token should be passed in the form of a cookie as below
cookies = {}
cookies['APIC-cookie'] = token

put_url = "https://10.10.20.58/api/node/mo/sys/intf/phys-[eth1/97].json"

# Editing the description of the interface in the payload
payload = "{\n    \"l1PhysIf\":{\n        \"attributes\":{\n            \"descr\":\"\"\n        }\n    }\n}"
headers = {
    'Content-Type': 'application/json',
}

# Adding the cookie into the headers
put_response = requests.put(
    put_url, headers=headers, data=payload, cookies=cookies, verify=False).json()

pprint(put_response)
