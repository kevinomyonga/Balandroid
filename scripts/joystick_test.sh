#!/bin/sh

# Install Joystick Package
sudo apt-get install joystick -y

# Joystick Package - Test js0
sudo jstest /dev/input/js0

