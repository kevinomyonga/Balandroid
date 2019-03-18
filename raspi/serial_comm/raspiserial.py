#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file presents an interface for interacting with the Arduino micro controller
# in Python. Simply plug your Arduino into your computer using USB and run this
# script!
#
# Copyright © 2019 Kevin N. Omyonga <komyonga@gmail.com>

import serial
import time

class RasPiSerial(object):
    
    try:
        intfName = "/dev/ttyACM0"
        baudRate = 9600
        ser = serial.Serial(intfName, baudRate, timeout = 0.1)
        delay = 0.1
        print('RasPi Arduino Serial Connection Established')
    except Exception as err:
        print('An exception occured while listening for the Arduino')
        print(str(err))

    #if you only want to send data to arduino (i.e. a signal to move a servo)
    def send(self, theinput):
        self.ser.write(theinput.encode())
        time.sleep(self.delay)

    #if you would like to tell the arduino that you would like to receive data from the arduino
    def send_and_receive(self, theinput):
        self.ser.flushInput()
        self.ser.flushOutput()
        self.ser.write(theinput.encode())
        
        while True:
            try:
                time.sleep(self.delay)
                state = self.ser.readline()
                # print state
                return state
            except:
                pass
            time.sleep(self.delay)


if __name__ == "__main__":
    arduino = RasPiSerial()
