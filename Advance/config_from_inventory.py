#####
# Created by: 	  Trishul Baxi
# Project: 	      Data Center Python automation
# Calssification:  Personal Project
#####


import time
import yaml
from netmiko import ConnectHandler
from getpass import getpass  # User needs to login. Avoids storing passwords in plain text.


start = time.time()  # start time of executing this script

#################

# Load device information from the YAML file
with open('inventory.yaml', 'r') as file:
    inventory = yaml.safe_load(file)

# Check to confirm python has read the yaml file correctly
print(inventory)

#################
# Function to get the information for a specific device
def get_device_info(inventory, device_name):
    leaf_switches = inventory.get('leaf_switches', [])
    spine_switches = inventory.get('spine_switches', [])
    for device in leaf_switches:
        if device_name in device:
            return device[device_name]
    for device in spine_switches:
        if device_name in device:
            return device[device_name]
    raise ValueError(f"Device {device_name} not found in the inventory.")

#################

# Read configuration commands from a text file
def read_config(file_name):
    with open(file_name, 'r') as file:
        return file.read().splitlines()

#################

# Function to connect and apply configuration
def connect_and_configure(device_info, config_commands,  password):
        # Update the device_info dictionary with the password
        device_info['password'] = password
        connection = ConnectHandler(**device_info)
        connection.enable()
        output = connection.send_config_set(config_commands)
        print(output)
        connection.disconnect()

#################

# create a variable to store the password from user input.
password = getpass()

#################

# Device and config file mappings
devices_and_configs = {
    'leaf1': 'configs/leaf1.txt',
    'leaf2': 'configs/leaf2.txt',
    'leaf3': 'configs/leaf3.txt',
    'spine1': 'configs/spine1.txt',
    'spine2': 'configs/spine2.txt'
}

#################

# Applying the config to the swithes from the dictionary above
for device_name, config_file in devices_and_configs.items():
     device_info = get_device_info(inventory, device_name)
     config_commands = read_config(config_file)
     connect_and_configure(device_info, config_commands, password)

#################

# Final execution time
end = time.time() # Stop time of executing this script
print( f'TOTAL EXECUTION TIME = {end-start:.2f} seconds')

#################