#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file presents an interface for interacting with the Raspberry Pi Camera module
# in Python.
#
# Copyright © 2019 Kevin N. Omyonga <komyonga@gmail.com>

# import the necessary packages
import os
import datetime as dt
#from picamera.array import PiRGBArray
from picamera import PiCamera
import time
#import cv2

class BalandroidCam(object):
    
    try:
        # initialize the camera and grab a reference to the raw camera capture
        camera = PiCamera()
        #rawCapture = PiRGBArray(camera)
        
        # allow the camera to warmup
        delay = 0.1
        time.sleep(delay)
        print('RasPi Camera Connection Established')
    except:
        print('An Exception Occured While Listening For The Camera')

    destination = '/home/pi/Desktop/'
    
    def capture_image(self):
        filename = os.path.join(self.destination, dt.datetime.now().strftime('%Y-%m-%d_%H.%M.%S.jpg'))
        self.camera.start_preview()
        self.camera.capture(filename)
        self.camera.stop_preview()
    
    def record_video(self):
        filename = os.path.join(destination, dt.datetime.now().strftime('%Y-%m-%d_%H.%M.%S.h264'))
        camera.start_preview()
        camera.start_recording(filename)

    def finish_video(self):
        camera.stop_recording()
        camera.stop_preview()
    
    
if __name__ == "__main__":
    balandroidcam = BalandroidCam()
    balandroidcam.capture_image()

