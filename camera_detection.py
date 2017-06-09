import cv2
import numpy as np
from pynq.board import Switch
from pynq import Overlay
Overlay("base.bit").download()

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 5, (640,480))

#for red color
# lower mask (0-10)
lower_1 = np.array([0,50,50])
upper_1 = np.array([10,255,255])
# upper mask (170-180)
lower_2 = np.array([170,50,50])
upper_2 = np.array([180,255,255])


if not cap.isOpened():
    print('Camera is not open.')

while True:
    if Switch(0).read():
        print ('switch 0 read')
        break
    ret, frame = cap.read()
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask0 = cv2.inRange(hsv, lower_1, upper_1)
        mask1 = cv2.inRange(hsv, lower_2, upper_2)
        mask = mask0 + mask1
        hsv = cv2.bitwise_and(hsv, hsv, mask= mask)
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            #center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            if radius > 10:
                cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
                cv2.circle(frame, (int(x), int(y)), 5, (0, 0, 255), -1)
                print (int(x), int(y))
        out.write(frame)
            
print('stop')
cap.release()
out.release()
