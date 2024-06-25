import os
import json
import requests
import uvicon
from typing import Union
from fastapi import FastAPI,File,UploadFile,Request,Form
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import smbus
from board import SCL, SDA
from adafruit_motor import servo
from gpiozero.pins.pigpio import PiGPIOFactory 
import serial
app = FastAPI()


try:
	bldc_ACM0 = serial.Serial("/dev/ttyACM0")
except:
	print('No bldc_ACM0 device found')

try:
	servo_ACM0_0 = serial.Serial("/dev/ttyACM0")
except:
	print('No servo_ACM0_0 device found')





































