from netmiko import ConnectHandler
from getpass import getpass  # User needs to lodgin. Avoids storing passwords in plain text.

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

# Configure OSPF on leafs
for devices in leafs:
    net_connect = ConnectHandler(**devices)
    net_connect.enable()

    cmd = '''
    feature ospf

    int loop 99
    ip router ospf TEST-DC area 0

    int eth1/53
    no sw
    ip router ospf TEST-DC area 0
    ip ospf network point-to-point
    no ip ospf passive-interface
    no shut

    int eth1/54
    no sw
    ip router ospf TEST-DC area 0
    ip ospf network point-to-point
    no ip ospf passive-interface
    no shut

    router ospf TEST-DC
    passive-interface default

    '''
    output = net_connect.send_config_set(cmd.split('\n'))
    print (output)  # Print the output to your screen.

#################

#Configure individual loopbak ip addresses
net_connect = ConnectHandler(**leaf1)
net_connect.enable()

cmd = ''' 
int loop 99
Description configured by Python 
ip address 11.11.11.11 255.255.255.255

int eth1/53
Description configured by Python - TO SPINE 1
ip address 192.168.10.1 255.255.255.252

int eth1/54
Description configured by Python - TO SPINE 2
ip address 192.168.20.1 255.255.255.252

router ospf TEST-DC
router-id 91.91.91.91

'''
output = net_connect.send_config_set(cmd.split('\n'))
print (output)  # Print the output to your screen.

#################

#Configure individual loopbak ip addresses
net_connect = ConnectHandler(**leaf2)
net_connect.enable()

cmd = ''' 
int loop 99
Description configured by Python 
ip address 22.22.22.22 255.255.255.255

int eth1/53
no sw
Description configured by Python - TO SPINE 1
ip address 192.168.10.5 255.255.255.252

int eth1/54
no sw
Description configured by Python - TO SPINE 2
ip address 192.168.20.5 255.255.255.252

router ospf TEST-DC
router-id 92.92.92.92

'''
output = net_connect.send_config_set(cmd.split('\n'))
print (output)  # Print the output to your screen.

#################

#Configure individual loopbak ip addresses
net_connect = ConnectHandler(**leaf3)
net_connect.enable()

cmd = ''' 
int loop 99
Description configured by Python 
ip address 33.33.33.33 255.255.255.255

int eth1/53
no sw
Description configured by Python - TO SPINE 1
ip address 192.168.10.9 255.255.255.252

int eth1/54
no sw
Description configured by Python - TO SPINE 2
ip address 192.168.20.9 255.255.255.252

router ospf TEST-DC
router-id 93.93.93.93

'''
output = net_connect.send_config_set(cmd.split('\n'))
print (output)  # Print the output to your screen.

#################



