#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file presents an interface for interacting with the XBox One Controller
# in Python. Simply plug your XBOX controller into your computer using USB and run this
# script!
#
# NOTE: I assume in this script that the only joystick plugged in is the XBox One controller.
#       if this is not the case, you will need to change the class accordingly.
#
# Copyright © 2019 Kevin N. Omyonga <komyonga@gmail.com>

import os
import pprint
import pygame

from constants import *
from serial_comm.raspiserial import *
from image_processing.balandroidcam import *

class XBOXController(object):
    """Class representing the XBOX controller. Pretty straightforward functionality."""

    controller = None
    axis_data = None
    button_data = None
    hat_data = None
    
    arduino = None
    raspi_camera = None

    def init(self):
        """Initialize the joystick components"""
        
        pygame.init()

        try:
            pygame.joystick.init()
            self.controller = pygame.joystick.Joystick(0)
            self.controller.init()
            print ('Joystick Found - Connection Established')
            self.arduino = RasPiSerial()
            self.raspi_camera = BalandroidCam()
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
                        if event.button == PS4_SQUARE:
                            print ('Pressed the SQUARE button')
                        if event.button == X:
                            print ('Pressed the X button')
                        if event.button == PS4_CIRCLE:
                            print ('Pressed the CIRCLE button')
                        if event.button == PS4_TRIANGLE:
                            print ('Pressed the TRIANGLE button')
                        if event.button == PS4_L1:
                            print ('Pressed the L1 button')
                        if event.button == PS4_R1:
                            print ('Pressed the R1 button')
                        if event.button == PS4_L2:
                            print ('Pressed the L2 button')
                        if event.button == PS4_R2:
                            print ('Pressed the R2 button')
                        if event.button == PS4_SHARE:
                            print ('Pressed the SHARE button')
                        if event.button == PS4_OPTIONS:
                            print ('Pressed the OPTIONS button')
                        if event.button == PS4_L3:
                            print ('Pressed the L3 button')
                        if event.button == PS4_R3:
                            print ('Pressed the R3 button')
                        if event.button == PS4_ON_BUTTON:
                            print ('Pressed the PS4 button')
                        if event.button == PS4_TOUCHPAD_PRESS:
                            print ('Pressed the TOUCHPAD button')
                    elif event.type == pygame.JOYBUTTONUP:
                        if event.button == PS4_SQUARE:
                            print ('Released the SQUARE button')
                        if event.button == PS4_X:
                            print ('Released the X button')
                        if event.button == PS4_CIRCLE:
                            print ('Released the CIRCLE button')
                        if event.button == PS4_TRIANGLE:
                            print ('Released the TRIANGLE button')
                        if event.button == PS4_L1:
                            print ('Released the L1 button')
                        if event.button == PS4_R1:
                            print ('Released the R1 button')
                        if event.button == PS4_L2:
                            print ('Released the L2 button')
                        if event.button == PS4_R2:
                            print ('Released the R2 button')
                        if event.button == PS4_SHARE:
                            print ('Released the SHARE button')
                        if event.button == PS4_OPTIONS:
                            print ('Released the OPTIONS button')
                        if event.button == PS4_L3:
                            print ('Released the L3 button')
                        if event.button == PS4_R3:
                            print ('Released the R3 button')
                        if event.button == PS4_ON_BUTTON:
                            print ('Released the PS4 button')
                        if event.button == PS4_TOUCHPAD_PRESS:
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
    xbox = XBOXController()
    xbox.init()
    xbox.listen()


