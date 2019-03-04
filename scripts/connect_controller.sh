#!/bin/sh

# Bluetooth command line tool
sudo bluetoothctl

# Enable the agent and set the agent to the default
agent on
default-agent

# Start scanning for devices
scan on

# Make a connection with your PS4 controller
read -r -p "Enter Controller MAC Address: " address
connect $address

# Add our MAC address to the trusted list 
# so the PS4 controller can automatically connect
trust $address
