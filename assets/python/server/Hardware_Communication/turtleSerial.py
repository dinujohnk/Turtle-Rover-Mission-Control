#!/usr/bin/python3

import numpy as np  #   data types

import sys
import os
import time
import serial

ser = serial.Serial("/dev/serial0")
ser.baudrate = 115200

def sendSerial (message):
    print(message)
    #message = [chr(i) for i in message]     # convert to integers
    #message = ''.join(message)
    #print(message)
    ser.write(bytearray(message))
    return
