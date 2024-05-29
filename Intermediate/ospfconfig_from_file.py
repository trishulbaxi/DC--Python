#####
# Created by: 	  Trishul Baxi
# Project: 	      Data Center Python automation
# Calssification:  Personal Project
#####


from netmiko import ConnectHandler
from getpass import getpass  # User needs to login. Avoids storing passwords in plain text.
import time

start = time.time()  # start time of executing this script

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

#################

# INTERFACE & OSPF CONFIGURATION - SPINE

#################

# Connect to devices & enter enable mode
net_connect = ConnectHandler(**spine1)
net_connect.enable()

# Apply interface & OSPF configuration & save to a variable to print on screen
output = net_connect.send_config_from_file('configs/spine1.txt')
print (output)  # Print the output to your screen.

#################

# Connect to devices & enter enable mode
net_connect = ConnectHandler(**spine2)
net_connect.enable()

# Apply interface & OSPF configuration & save to a variable to print on screen
output = net_connect.send_config_from_file('configs/spine2.txt')
print (output)  # Print the output to your screen.

#################

# INTERFACE & OSPF CONFIGURATION - LEAF

#################

# Connect to devices & enter enable mode
net_connect = ConnectHandler(**leaf1)
net_connect.enable()

# Apply interface & OSPF configuration & save to a variable to print on screen
output = net_connect.send_config_from_file('configs/leaf1.txt')
print (output)  # Print the output to your screen.

#################

# Connect to devices & enter enable mode
net_connect = ConnectHandler(**leaf2)
net_connect.enable()

# Apply interface & OSPF configuration & save to a variable to print on screen
output = net_connect.send_config_from_file('configs/leaf2.txt')
print (output)  # Print the output to your screen.

#################

# Connect to devices & enter enable mode
net_connect = ConnectHandler(**leaf3)
net_connect.enable()

# Apply interface & OSPF configuration & save to a variable
output = net_connect.send_config_from_file('configs/leaf3.txt')
print (output)  # Print the output to your screen.

#################

end = time.time() # Stop time of running this script
print( f'TOTAL EXECUTION TIME = {end-start} seconds')