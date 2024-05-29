#####
# Created by: 	  Trishul Baxi
# Project: 	      Data Center Python automation
# Calssification:  Personal Project
#####

# Configuring OSPF on one device

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
feature ospf

int loop 99
Description configured by Python 
ip address 100.100.100.100 255.255.255.255
ip router ospf TEST-DC area 0

int eth1/53
no sw
Description configured by Python - TO SPINE 1
ip address 192.168.10.1 255.255.255.252
ip router ospf TEST-DC area 0
ip ospf network point-to-point
no ip ospf passive-interface
no shut

int eth1/54
no sw
Description configured by Python - TO SPINE 2
ip address 192.168.20.1 255.255.255.252
ip router ospf TEST-DC area 0
ip ospf network point-to-point
no ip ospf passive-interface
no shut

router ospf TEST-DC
router-id 10.10.10.10
passive-interface default

'''
output = net_connect.send_config_set(cmd.split('\n'))
print (output)  # Print the output to your screen.
