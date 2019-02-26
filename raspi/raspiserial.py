#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file presents an interface for interacting with the Arduino micro controller
# in Python. Simply plug your Arduino into your computer using USB and run this
# script!
#
# Copyright © 2019 Kevin N. Omyonga <komyonga@gmail.com>
#
# Distributed under terms of the MIT license.

import serial
import time

class RasPiSerial(object):
    
    try:
        intfName = "/dev/ttyACM0"
        baudRate = 9600
        ser = serial.Serial(intfName, baudRate, timeout = 0.1)
        delay = 0.1
    except:
        print('An exception occured while listening for the Arduino')

    #if you only want to send data to arduino (i.e. a signal to move a servo)
    def send(self, theinput):
        self.ser.write(theinput)
        time.sleep(delay)

    #if you would like to tell the arduino that you would like to receive data from the arduino
    def send_and_receive(self, theinput):
        self.ser.flushInput()
        self.ser.flushOutput()
        self.ser.write(theinput)
        
        while True:
            try:
                time.sleep(delay)
                state = self.ser.readline()
                # print state
                return state
            except:
                pass
            time.sleep(delay)


if __name__ == "__main__":
    arduino = RasPiSerial()
