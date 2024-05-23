
from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

sw1 = {
    'device_type': "cisco_nxos",
    'ip': '192.168.90.3',
    'username': 'admin',
    'password': password,
    #'secret': password,
}

net_connect = ConnectHandler(**sw1)
net_connect.enable()
config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.255', 'Description Python Loopback']
output = net_connect.send_config_set(config_commands)
print (output)
