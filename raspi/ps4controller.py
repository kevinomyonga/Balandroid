#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file presents an interface for interacting with the Playstation 4 Controller
# in Python. Simply plug your PS4 controller into your computer using USB and run this
# script!
#
# NOTE: I assume in this script that the only joystick plugged in is the PS4 controller.
#       if this is not the case, you will need to change the class accordingly.
#
# Copyright © 2019 Kevin N. Omyonga <komyonga@gmail.com>

# PS4 Controller Button Numbering
'''
=============================
No. |   Desination          |
*****************************
0   =   SQUARE              |
1   =   X                   |
2   =   CIRCLE              |
3   =   TRIANGLE            |
4   =   L1                  |
5   =   R1                  |
6   =   L2                  |
7   =   R2                  |
8   =   SHARE               |
9   =   OPTIONS             |
10  =   LEFT ANALOG PRESS   |
11  =   RIGHT ANALOG PRESS  |
12  =   PS4 ON BUTTON       |
13  =   TOUCHPAD PRESS      |
*****************************
'''

import os
import pprint
import pygame

from raspiserial import *

class PS4Controller(object):
    """Class representing the PS4 controller. Pretty straightforward functionality."""

    controller = None
    axis_data = None
    button_data = None
    hat_data = None
    arduino = None

    def init(self):
        """Initialize the joystick components"""
        
        pygame.init()

        try:
            pygame.joystick.init()
            self.controller = pygame.joystick.Joystick(0)
            self.controller.init()
            print ('Joystick Found - Connection Established')
            self.arduino = RasPiSerial()
        except pygame.error:
            print ('No Joystick Found')

    def listen(self):
        
        try:
            """Listen for events to happen"""
        
            if not self.axis_data:
                self.axis_data = {}

            if not self.button_data:
                self.button_data = {}
                for i in range(self.controller.get_numbuttons()):
                    self.button_data[i] = False

            if not self.hat_data:
                self.hat_data = {}
                for i in range(self.controller.get_numhats()):
                    self.hat_data[i] = (0, 0)

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.JOYAXISMOTION:
                        if event.axis == 0:
                            if event.value > 0:
                                print ('right')
                            if event.value < 0:
                                print ('left')
                        if event.axis == 1:
                            if event.value > 0:
                                print ('down')
                            if event.value < 0:
                                print ('up')
                    elif event.type == pygame.JOYBUTTONDOWN:
                        if event.button == 0:
                            print ('Pressed the SQUARE button')
                        if event.button == 1:
                            print ('Pressed the X button')
                        if event.button == 2:
                            print ('Pressed the CIRCLE button')
                        if event.button == 3:
                            print ('Pressed the TRIANGLE button')
                        if event.button == 4:
                            print ('Pressed the L1 button')
                        if event.button == 5:
                            print ('Pressed the R1 button')
                        if event.button == 6:
                            print ('Pressed the L2 button')
                        if event.button == 7:
                            print ('Pressed the R2 button')
                        if event.button == 8:
                            print ('Pressed the SHARE button')
                        if event.button == 9:
                            print ('Pressed the OPTION button')
                        if event.button == 10:
                            print ('Pressed the L3 button')
                        if event.button == 11:
                            print ('Pressed the R3 button')
                        if event.button == 12:
                            print ('Pressed the PS4 button')
                        if event.button == 13:
                            print ('Pressed the TOUCHPAD button')
                    elif event.type == pygame.JOYBUTTONUP:
                        if event.button == 0:
                            print ('Released the SQUARE button')
                        if event.button == 1:
                            print ('Released the X button')
                        if event.button == 2:
                            print ('Released the CIRCLE button')
                        if event.button == 3:
                            print ('Released the TRIANGLE button')
                        if event.button == 4:
                            print ('Released the L1 button')
                        if event.button == 5:
                            print ('Released the R1 button')
                        if event.button == 6:
                            print ('Released the L2 button')
                        if event.button == 7:
                            print ('Released the R2 button')
                        if event.button == 8:
                            print ('Released the SHARE button')
                        if event.button == 9:
                            print ('Released the OPTION button')
                        if event.button == 10:
                            print ('Released the L3 button')
                        if event.button == 11:
                            print ('Released the R3 button')
                        if event.button == 12:
                            print ('Released the PS4 button')
                        if event.button == 13:
                            print ('Released the TOUCHPAD button')
                    elif event.type == pygame.JOYHATMOTION:
                        if event.hat == 0:
                            if event.value == (1, 0):
                                print ('right')
                            if event.value == (-1, 0):
                                print ('left')
                            if event.value == (0, 1):
                                print ('up')
                            if event.value == (0, -1):
                                print ('down')

                    # Insert your code on what you would like to happen for each event here!
                    # In the current setup, I have the state simply printing out to the screen.
                    
                    #os.system('clear')
                    #pprint.pprint(self.button_data)
                    #pprint.pprint(self.axis_data)
                    #pprint.pprint(self.hat_data)
             
        except KeyboardInterrupt:
            print('PROGRAM TERMINATED')
            self.controller.quit()
        except:
            print ('An exception occured while listening for the joystick')


if __name__ == "__main__":
    ps4 = PS4Controller()
    ps4.init()
    ps4.listen()

