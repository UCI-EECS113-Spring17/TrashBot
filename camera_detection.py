
import cv2
from matplotlib import pyplot as plt
import numpy as np
from pynq import Overlay
Overlay("base.bit").download()
from MotorFunctions import MFunction
import time


cap = cv2.VideoCapture(0)
obj_cascade = cv2.CascadeClassifier('haarcascade_shoe.xml')
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi',fourcc, 5, (640,480))
if cap.isOpened():
	while True:
		ret, frame = cap.read()
		if ret:
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			detection = obj_cascade.detectMultiScale(gray, 1.3, 5)
			if len(detection) != 0:
				print('Detect.')
				'''
				for (x, y, w, h) in detection:
					cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
				'''
				# detection location x, y
				loc_x = detection[0][0] + detection[0][2] / 2
				loc_y = detection[0][1] + detection[0][3] / 2				
				MFunction.goForward()
				
			else:
				print('Not detect')
				MFunction.stop()
			#out.write(frame)
            
print('stop')
cap.release()
#out.release()



			
