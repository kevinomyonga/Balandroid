#!/bin/sh

# Xbox Controller Driver
sudo apt-get install xboxdrv

# Allows the Xbox Controller to interact with the computer and will enable it to imitate the mouse
read -r -p "Control your Raspberry Pi with the Xbox controller?[y/N] " choice
case "$choice" in
[yY][eE][sS]|[yY])

sudo xboxdrv --detach-kernel-driver --silent --mouse
;;
*)
echo "Option Rejected"
;;
esac
