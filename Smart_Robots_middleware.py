print('Initialize project Smart_Robots')
import os
import json
import requests
import threading
from itertools import count
import serial
import cv2
import smbus
from mpu6050 import mpu6050




try:
	lidar_serial_ACM0 = serial.Serial("/dev/ttyACM0")
except:
	print('No lidar_serial_ACM0 device found')

try:
	cellular_network_ACM0 = serial.Serial("/dev/ttyACM0")
except:
	pass

camera_2 = cv2.VideoCapture(2)

camera_0 = cv2.VideoCapture(0)

imus_68 = mpu6050(0x68)


try:
	communication_network_ACM0 = serial.Serial("/dev/ttyACM0")
except:
	print('No communication_network_ACM0 device found')




def Lidar_serial_ACM0():
	pass

def Cellular_network_ACM0():
	pass

def Camera_2():
	pass

def Camera_0():
	pass



def Communication_network_ACM0():
	pass




t_lidar_serial_ACM0 = threading.Thread(target=Lidar_serial_ACM0)

t_cellular_network_ACM0 = threading.Thread(target=Cellular_network_ACM0)

t_camera_2 = threading.Thread(target=Camera_2)

t_camera_0 = threading.Thread(target=Camera_0)



t_communication_network_ACM0 = threading.Thread(target=Communication_network_ACM0)




t_lidar_serial_ACM0.start()

t_cellular_network_ACM0.start()

t_camera_2.start()

t_camera_0.start()



t_communication_network_ACM0.start()
