%matplotlib inline
import cv2
from matplotlib import pyplot as plt
import numpy as np
from pynq.board import Button
from pynq import Overlay
Overlay("base.bit").download()

cap = cv2.VideoCapture(0)
obj_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 5, (640,480))
if not cap.isOpened():
    print('Camera is not open.')

while cap.isOpened():
    if Button(0).read():
        break

    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detection = obj_cascade.detectMultiScale(gray, 1.3, 5)
        if len(detection) != 0:
            print('Detect.')
            for (x, y, w, h) in detection:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        else:
            print('Not detect')
        
        out.write(frame)
            
print('stop')
cap.release()
out.release()



			
