from netmiko import ConnectHandler
from getpass import getpass  # User needs to lodgin. Avoids storing passwords in plain text.
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

spines = [spine1, spine2]
leafs = [leaf1, leaf2, leaf3]

#################

#OSPF CONFIGURATION - INDIVIDUAL CONFIG FILES

#################

#Configure individual ip addresses
net_connect = ConnectHandler(**spine1)
net_connect.enable()

output = net_connect.send_config_from_file('spine1.txt')
print (output)  # Print the output to your screen.

#################

#Configure individual ip addresses
net_connect = ConnectHandler(**spine2)
net_connect.enable()

output = net_connect.send_config_from_file('spine2.txt')
print (output)  # Print the output to your screen.

#################

# LEAF CONFIGURATION

#################

#Configure individual ip addresses
net_connect = ConnectHandler(**leaf1)
net_connect.enable()

output = net_connect.send_config_from_file('leaf1.txt')
print (output)  # Print the output to your screen.

#################

#Configure individual ip addresses
net_connect = ConnectHandler(**leaf2)
net_connect.enable()

output = net_connect.send_config_from_file('leaf2.txt')
print (output)  # Print the output to your screen.

#################

#Configure individual ip addresses
net_connect = ConnectHandler(**leaf3)
net_connect.enable()

output = net_connect.send_config_from_file('leaf3.txt')
print (output)  # Print the output to your screen.

#################

end = time.time() # stop time of running this script
print( f'Total execution time = {end-start} seconds')