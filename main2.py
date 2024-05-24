#####
# Created by: 	  Trishul Baxi
# Project: 	      Data Center Python automation
# Calssification:  Personal Project
#####


from netmiko import ConnectHandler  # use netmiko for SSH connections.
from getpass import getpass  # User needs to lodgin. Avoids storing passwords in plain text.

password = getpass()   # create a variable to store the password input.

# Define the device connection parameters in a dictionary.
sw1 = {
    'device_type': "cisco_nxos",
    'ip': '192.168.90.3',
    'username': 'admin',
    'password': password,
    #'secret': password,   # optional if you do not create a network-admin role on the Cisco device
}

# Connect to the device and apply the configuration.
net_connect = ConnectHandler(**sw1)
net_connect.enable()

cmd = '''
int loop 0 
Description Python Loopback
ip address 1.1.1.1 255.255.255.255 

int loop 100
Description Python Loopback
ip address 100.100.100.100 255.255.255.255
'''
output = net_connect.send_config_set(cmd.split('\n'))
print (output)  # Print the output to your screen.
