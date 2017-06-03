#File: face_detect_test1.py
#Course: EECS 113 Processor HW/SW Interface, Spring 2017
#Team: TrashBot
#Members:
#     Linda Vang
#     Claudia Gorgonio
#     Jun Li
#     Sandra Fong
#Description:
#     Test file for Webcam Face Detection


from pynq import Overlay
Overlay("base.bit").download()
from pynq.drivers.video import Frame
import cv2
import numpy as np
%matplotlib inline 
from matplotlib import pyplot as plt
import time

face_cascade = cv2.CascadeClassifier(
                        'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(
                        'haarcascade_eye.xml')
profile_cascade = cv2.CascadeClassifier(
                        'haarcascade_profileface.xml')
facealt_cascade = cv2.CascadeClassifier(
                        'haarcascade_frontalface_alt.xml')
facealt2_cascade = cv2.CascadeClassifier(
                        'haarcascade_frontalface_alt2.xml')

frame_in_w = 640
frame_in_h = 480

videoIn = cv2.VideoCapture(0)
videoIn.set(cv2.CAP_PROP_FRAME_WIDTH, frame_in_w);
videoIn.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_in_h);

print("capture device is open: " + str(videoIn.isOpened()))

for i in range(0, 4):
    f_x = 0
    f_y = 0
    fa_x = 0
    fa_y = 0
    fa2_x = 0
    fa2_y = 0
    p_x = 0
    p_y = 0
    f_len = 0
    fa_len = 0
    fa2_len = 0
    p_len = 0
    avg_counter = 0
    avg_len = 0
    ret, frame_vga = videoIn.read()

#%matplotlib inline 
#from matplotlib import pyplot as plt
# Display webcam image via HDMI Out
#if (ret):
#    frame_1080p = np.zeros((1080,1920,3)).astype(np.uint8)       
#    frame_1080p[0:480,0:640,:] = frame_vga[0:480,0:640,:]
#else:
#    print("Error while reading from camera")
    
    #plt.imshow(frame_vga[:,:,[2,1,0]])
    #plt.show()

    #np_frame = frame_vga
    gray = cv2.cvtColor(frame_vga, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces) == 0:
        print("no face is detected: ", i)
    else:
        print("face is detected: ", i)
        print(faces)
        f_x = faces[0][0]
        f_y = faces[0][1]
        f_len = faces[0][2]
        print("fx and fy is: ", f_x, f_y)
        avg_counter += 1
        print("")
    #faces is in blue
    for (x,y,w,h) in faces:
        cv2.rectangle(frame_vga,(x,y),(x+w,y+h),(255,0,0),2)
        #roi_gray = gray[y:y+h, x:x+w]
        #roi_color = frame_vga[y:y+h, x:x+w]
        #eyes = eye_cascade.detectMultiScale(roi_gray)
        #for (ex,ey,ew,eh) in eyes:
            #eyes is in green
            #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    facesalt = facealt_cascade.detectMultiScale(gray, 1.3, 5)
    if len(facesalt) == 0:
        print("no facealt is detected: ", i)
    else:
        print("facealt is detected: ", i)
        print(facesalt)
        fa_x = facesalt[0][0]
        fa_y = facesalt[0][1]
        fa_len = facesalt[0][2]
        print("fax and fay is: ", fa_x, fa_y)
        avg_counter += 1
        print("")
    #facesalt is in purple
    for (x,y,w,h) in facesalt:
        cv2.rectangle(frame_vga,(x,y),(x+w,y+h),(128,0,128),2)
        
    facesalt2 = facealt2_cascade.detectMultiScale(gray, 1.3, 5)
    if len(facesalt2) == 0:
        print("no facealt2 is detected: ", i)
    else:
        print("facealt2 is detected: ", i)
        print(facesalt2)
        fa2_x = facesalt2[0][0]
        fa2_y = facesalt2[0][1]
        fa2_len = facesalt2[0][2]
        print("fa2x and fa2y is: ", fa2_x, fa2_y)
        avg_counter += 1
        print("")
    #facesalt is in pink
    for (x,y,w,h) in facesalt2:
        cv2.rectangle(frame_vga,(x,y),(x+w,y+h),(255,192,203),2)

    profiles = profile_cascade.detectMultiScale(gray, 1.3, 5)
    if len(profiles) == 0:
        print("no profile is detected: ", i)
    else:
        print("profile is detected: ", i)
        print(profiles)
        p_x = profiles[0][0]
        p_y = profiles[0][1]
        p_len = profiles[0][2]
        print("px and py is: ", p_x, p_y)
        avg_counter += 1
        print("")
    #profiles is in red
    for (x,y,w,h) in profiles:
        cv2.rectangle(frame_vga,(x,y),(x+w,y+h),(0,0,255),2)

    if avg_counter != 0:
        print("")
        print("avg_counter is: ", avg_counter)
        avg_x = f_x+fa_x+fa2_x+p_x
        avg_x = avg_x/avg_counter
        #avg_y = f_y+fa_y+fa2_y+p_y
        #avg_y = avg_y/avg_counter
        print("avg_x is: ", avg_x)
    
        avg_len = f_len+fa_len+fa2_len+p_len
        avg_len = avg_len/avg_counter
        print("avg_len is: ", avg_len)
        if avg_x < 200:
            if avg_len < 150:
                print("move left&forward")
                #return 1 to indicate left&forward movement needed
            elif avg_len > 250:
                print("move left&back")
                #return 2 to indicate left&back movment needed
            else:
                print("move left")
                #return 3 to indicate left movement needed
        elif avg_x > 300:
            if avg_len < 150:
                print("move right&forward")
                #return 4 to indicate right&forward movement needed
            elif avg_len > 250:
                print("move right&back")
                #return 5 to indicate right&back movment needed
            else:
                print("move right")
                #return 6 to indicate right movement needed
        elif avg_len < 150:
            print("move forward")
            #return 7 to indicate forward movement needed
        elif avg_len > 250:
            print("move back")
            #return 8 to indicate back movment needed  
        else:
            print("don't move")
            #return 0 to indicate no movement needed
        
    else:
        print("don't move")
        #return 0 to indicate no movement needed 
    
    plt.imshow(frame_vga[:,:,[2,1,0]])
    plt.show()
    time.sleep(1)
    #k = cv2.waitKey(30) & 0xff
    #if k == 27:
     #   break
        
# Output OpenCV results via matplotlib
#%matplotlib inline 
#from matplotlib import pyplot as plt
#import numpy as np
#plt.imshow(np_frame[:,:,[2,1,0]])
#plt.show()

videoIn.release()
#cv2.destroyAllWindows()