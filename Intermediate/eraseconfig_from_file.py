from netmiko import ConnectHandler
from getpass import getpass  # User needs to login. Avoids storing passwords in plain text.
import time

start = time.time()  # start time of running this script

password = getpass()   # create a variable to store the password input.

leaf1 = {
    'device_type': "cisco_nxos",
    'ip': '192.168.90.3',
    'username': 'admin',
    'password': password,
    #'secret': password,   # optional if you do not create a network-admin role on the Cisco device
}

leaf2 = {
    'device_type': "cisco_nxos",
    'ip': '192.168.90.4',
    'username': 'admin',
    'password': password,
    #'secret': password,   # optional if you do not create a network-admin role on the Cisco device
}

leaf3 = {
    'device_type': "cisco_nxos",
    'ip': '192.168.90.5',
    'username': 'admin',
    'password': password,
    #'secret': password,   # optional if you do not create a network-admin role on the Cisco device
}

spine1 = {
    'device_type': "cisco_nxos",
    'ip': '192.168.90.1',
    'username': 'admin',
    'password': password,
    #'secret': password,   # optional if you do not create a network-admin role on the Cisco device
}

spine2 = {
    'device_type': "cisco_nxos",
    'ip': '192.168.90.2',
    'username': 'admin',
    'password': password,
    #'secret': password,   # optional if you do not create a network-admin role on the Cisco device
}

dc = [leaf1, leaf2, leaf3, spine1, spine2]

#################

# INTERFACE & OSPF CONFIGURATION - SPINE

#################

# Connect to all devices & enter enable mode
for devices in dc:
    net_connect = ConnectHandler(**devices)
    net_connect.enable()

    # Apply interface & OSPF configuration & save to a variable to print on screen
    output = net_connect.send_config_from_file('erase.txt')
    print(output)  # Print the output to your screen.

#################

