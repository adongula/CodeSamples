import meraki
import json
from pprint import pprint
# import logging
# logging.basicConfig(level=logging.DEBUG)

# CREATE Connection Object
x_cisco_meraki_api_key = '9103a4d27fc670d50f63f9d6047c0de121f475f1'  # Demo DevNet Sandbox
dashboard = meraki.DashboardAPI(api_key=(x_cisco_meraki_api_key))

# Get Orgs
orgs = dashboard.organizations.getOrganizations()
print(json.dumps(orgs, indent=2, sort_keys=True))
# pprint(orgs)

# Set OrgId
for org in orgs:
    if org['name'] == "DevNet Sandbox":
        orgId = org['id']

# Get Networks in Org
networks = dashboard.organizations.getOrganizationNetworks(orgId)

# Set NetworkId
for network in networks:
    if network['name'] == "DNSMB3-axxxxxagmail.com":
        netId = network['id']

# GET VLANS
vlans = dashboard.appliance.getNetworkApplianceVlans(netId)

# EXTRACTING THE VLAN TO BE UPDATED IN A SEPERATE DICTIONARY
vlan = vlans[1]

# UPDATING THE VLAN NAME TO 'Default'
result = dashboard.appliance.updateNetworkApplianceVlan(
    networkId=vlan['networkId'], vlanId=vlan['id'], name='Default')

# VERIFY
vlans = dashboard.appliance.getNetworkApplianceVlans(netId)
pprint(vlans)
