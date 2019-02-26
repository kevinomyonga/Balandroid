#!/bin/sh

# Install Joystick Package
sudo apt-get install joystick -y

# Joystick Package - Test js0
#sudo jstest /dev/input/js0

# Necessary Python3 Components
sudo apt-get install python3-dev python3-pip

# PS4 Controller Driver
sudo pip3 install ds4drv

# Setup the Raspberry Pi so non-root users can gain access to the joystick device that ds4drv creates
sudo wget https://raw.githubusercontent.com/chrippa/ds4drv/master/udev/50-ds4drv.rules -O /etc/udev/rules.d/50-ds4drv.rules
sudo udevadm control --reload-rules
sudo udevadm trigger

# Launch ds4drv At Startup
read -r -p "Automatically Launch ds4drv At Startup?[y/N] " choice
case "$choice" in
[yY][eE][sS]|[yY])
PATTERN="/usr/local/bin/ds4drv"
FILE="/etc/rc.local"

if grep -q $PATTERN $FILE;
then
echo "Startup Option Already Configured"
else
sudo sed -i -e '$i /usr/local/bin/ds4drv --hidraw --led 000008 &' /etc/rc.local
fi
;;
*)
echo "Startup Option Rejected"
;;
esac
