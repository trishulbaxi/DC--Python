#####
# Created by: 	  Trishul Baxi
# Project: 	      Data Center Python automation
# Calssification: Personal Project
#####


from netmiko import ConnectHandler  # use netmiko for SSH connections.
from getpass import getpass  # User needs to lodgin. Avoids storing passwords in plain text.

password = getpass()   # create a variable to store the password input.

# Define the device connection parameters in a list.
sw1 = {
    'device_type': "cisco_nxos",
    'ip': '192.168.90.3',
    'username': 'admin',
    'password': password,
    #'secret': password,
}

# Connect to the device and apply the configuration.
net_connect = ConnectHandler(**sw1)
net_connect.enable()
config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.255', 'Description Python Loopback']
output = net_connect.send_config_set(config_commands)
print (output)  # Print the output to your screen.
