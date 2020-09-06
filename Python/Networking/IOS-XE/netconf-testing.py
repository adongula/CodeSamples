from ncclient import manager
import xmltodict

router = {"host": "10.10.20.48", "port": "830",
          "username": "developer", "password": "C1sco12345"}

netconf_filter = '''
<filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>GigabitEthernet2</name>
        </interface>
    </interfaces>
    <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>GigabitEthernet2</name>
        </interface>
    </interfaces-state>
</filter>'''

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    print("Connected")
    # get the running config on the filtered out interface
    interface_netconf = m.get(netconf_filter)
    print("Getting the running-config of interfaces")

#XMLTODICT for converting xml output to a python dictionary
interface_python = xmltodict.parse(interface_netconf.xml)[
    "rpc-reply"]["data"]

interface_name = interface_python['interfaces']['interface']['name']['#text']
interface_desc = interface_python['interfaces']['interface']['description']

# If IP Address is not available, you will get an exception

# interface_ip = interface_python['interfaces']['interface']['ipv4']['address']['ip']
# interface_netmask = interface_python['interfaces']['interface']['ipv4']['address']['netmask']
interface_op_status = interface_python['interfaces-state']['interface']['oper-status']

print(f'Interface: {interface_name}')
print(f'Description: {interface_desc}')
# print(f'IP Address: {interface_ip}, Mask: {interface_netmask}')
print(f'Status: {interface_op_status}')




        