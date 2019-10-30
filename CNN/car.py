# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import cv2, time, sys, imutils, argparse
import RPi.GPIO as GPIO
from picamera.array import PiRGBArray
from picamera import PiCamera
import motor_control as mc

GPIO.setmode(GPIO.BCM)

#choose the GPIO pins for mptor control
fwd1 = 23 # pin 16
bwd1 = 24 #pin 18
fwd2 = 16 # pin 36
bwd2 = 20 # pin 38

# declare selected pin as output pin
GPIO.setup(fwd1, GPIO.OUT)
GPIO.setup(bwd1, GPIO.OUT)
GPIO.setup(fwd2, GPIO.OUT)
GPIO.setup(bwd2, GPIO.OUT)

model = load_model("model")

