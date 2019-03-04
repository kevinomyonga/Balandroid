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
        # Initialize the camera and grab a reference to the raw camera capture
        camera = PiCamera()
        #rawCapture = PiRGBArray(camera)
        
        # Allow the camera to warmup
        delay = 1
        time.sleep(delay)
        print('RasPi Camera Connection Established')
    except:
        print('An Exception Occured While Listening For The Camera')

    destination = '/home/pi/Desktop/Balandroid_Images'
    date_format = '%Y-%m-%d_%H.%M.%S'
    
    def capture_image(self):
        filename = os.path.join(self.destination, dt.datetime.now().strftime(self.date_format + '.jpg'))
        self.camera.start_preview()
        self.camera.capture(filename)
        self.camera.stop_preview()
        
    def capture_timelapse(self):
        # This will be used to name the pictures once stored.
        filename = os.path.join(self.destination, 'frame_' + dt.datetime.now().strftime(self.date_format + '.jpg'))
        timeInterval = 5 # The time interval between two pictures, in seconds
         
        #We have left all the settings in case you need to make some adjustments to improve the picture quality
        #self.camera.hflip = True
        #self.camera.vflip = True
        #camera.sharpness = 0
        #camera.contrast = 0
        #camera.brightness = 50
        #camera.saturation = 0
        #camera.ISO = 0
        #camera.video_stabilization = False
        #camera.exposure_compensation = 0
        #camera.exposure_mode = 'auto'
        #camera.meter_mode = 'average'
        #camera.awb_mode = 'auto'
        #camera.image_effect = 'none'
        #camera.color_effects = None
        #camera.rotation = 0
        #camera.crop = (0.0, 0.0, 1.0, 1.0)
         
        try:
            while True: #Infinite Loop
                filename = os.path.join(self.destination, 'frame_' + dt.datetime.now().strftime(self.date_format + '.jpg'))
                self.camera.capture(filename)
                print(filename)
                time.sleep(timeInterval)
        except KeyboardInterrupt: #Press Ctrl+C to interrupt
            pass
         
        print('All done...')
    
    def record_video(self):
        filename = os.path.join(destination, dt.datetime.now().strftime(self.date_format + '.h264'))
        camera.start_preview()
        camera.start_recording(filename)

    def finish_video(self):
        camera.stop_recording()
        camera.stop_preview()
    
    
if __name__ == "__main__":
    balandroidcam = BalandroidCam()
    #balandroidcam.capture_image()
    balandroidcam.capture_timelapse()

