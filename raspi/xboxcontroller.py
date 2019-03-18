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
                        if event.button == XBOX_A:
                            print ('Pressed the A button')
                        if event.button == XBOX_B:
                            print ('Pressed the B button')
                        if event.button == XBOX_X:
                            print ('Pressed the X button')
                        if event.button == XBOX_Y:
                            print ('Pressed the TRIANGLE button')
                        if event.button == XBOX_LB:
                            print ('Pressed the LB button')
                        if event.button == XBOX_RB:
                            print ('Pressed the RB button')
                        if event.button == XBOX_LT:
                            print ('Pressed the LT button')
                        if event.button == XBOX_RT:
                            print ('Pressed the RT button')
                        if event.button == XBOX_VIEW:
                            print ('Pressed the VIEW button')
                        if event.button == XBOX_MENU:
                            print ('Pressed the MENU button')
                        if event.button == XBOX_LTHUMBSTICK:
                            print ('Pressed the LTHUMBSTICK button')
                        if event.button == XBOX_RTHUMBSTICK:
                            print ('Pressed the RTHUMBSTICK button')
                    elif event.type == pygame.JOYBUTTONUP:
                        if event.button == XBOX_A:
                            print ('Released the A button')
                        if event.button == XBOX_B:
                            print ('Released the B button')
                        if event.button == XBOX_X:
                            print ('Released the X button')
                        if event.button == XBOX_Y:
                            print ('Released the TRIANGLE button')
                        if event.button == XBOX_LB:
                            print ('Released the LB button')
                        if event.button == XBOX_RB:
                            print ('Released the RB button')
                        if event.button == XBOX_LT:
                            print ('Released the LT button')
                        if event.button == XBOX_RT:
                            print ('Released the RT button')
                        if event.button == XBOX_VIEW:
                            print ('Released the VIEW button')
                        if event.button == XBOX_MENU:
                            print ('Released the MENU button')
                        if event.button == XBOX_LTHUMBSTICK:
                            print ('Released the LTHUMBSTICK button')
                        if event.button == XBOX_RTHUMBSTICK:
                            print ('Released the RTHUMBSTICK button')
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
        except Exception err:
            print ('An exception occured while listening for the joystick')
            print ('Error: '.format(err))


if __name__ == "__main__":
    xbox = XBOXController()
    xbox.init()
    xbox.listen()


