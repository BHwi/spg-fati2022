#!/usr/bin/env python
# coding: utf-8

# In[1]:


from zumi.zumi import Zumi
from zumi.util.camera import Camera
from zumi.util.screen import Screen
from zumi.util.color_classifier import ColorClassifier
import time

from threading import Thread
import IPython.display
import PIL.Image
from zumi.protocol import Note
from zumi.personality import Personality
import IPython.display
import datetime

camera = Camera()
screen = Screen()
zumi = Zumi()
from zumi.protocol import Note


# In[2]:


#도레미

zumi.play_note(Note.C4)
zumi.play_note(Note.D4)
zumi.play_note(Note.E4)


# In[3]:


#A

try:
    threshold = 40
    turnSpeed = 1
    forwardSpeed = 1

    while True:   
        bottom_right = zumi.read_IR('bottom_right')
        bottom_left = zumi.read_IR('bottom_left')
        
        if bottom_left > threshold and bottom_right > threshold :      
            zumi.control_motors(forwardSpeed,forwardSpeed,0)

        elif bottom_left > threshold and bottom_right < threshold :
            zumi.control_motors(turnSpeed,0,0)

        elif bottom_left < threshold and bottom_right > threshold:
            zumi.control_motors(0,turnSpeed,0)

        elif bottom_left > threshold :
            zumi.control_motors(turnSpeed,0,0)

        elif bottom_right > threshold :
            zumi.control_motors(0,turnSpeed,0)
            
        elif bottom_right < threshold  and bottom_left < threshold:
            zumi.stop()
            screen.draw_text_center("Stop")
            break
            
except KeyboardInterrupt:
    zumi.stop()
    print("The interrupt button was pressed.")
      
try:
    screen.draw_text_center("Zumi Start")
    user_name = 'hsy'
    demo_name = 'Acourse'

    knn = ColorClassifier(user_name=user_name)
    train = knn.load_model(demo_name)
    knn.fit("hsv")
    
    camera.start_camera()

    while True:    
            image = camera.capture()
            predict = knn.predict(image)
            screen.draw_text_center(predict)

            if predict == "orange":
                screen.draw_text_center("orange")
            if predict == "yellow":
                screen.draw_text_center("yellow")
            if predict == "blue":
                screen.draw_text_center("blue")
                
            zumi.forward(1, 1)
            break               
finally:
    camera.close()


# In[4]:


#빨강그린

try:
    threshold = 40
    turnSpeed = 1
    forwardSpeed = 1

    while True:   
        bottom_right = zumi.read_IR('bottom_right')
        bottom_left = zumi.read_IR('bottom_left')
        
        if bottom_left > threshold and bottom_right > threshold :      
            zumi.control_motors(forwardSpeed,forwardSpeed,0)

        elif bottom_left > threshold and bottom_right < threshold :
            zumi.control_motors(turnSpeed,0,0)

        elif bottom_left < threshold and bottom_right > threshold:
            zumi.control_motors(0,turnSpeed,0)

        elif bottom_left > threshold :
            zumi.control_motors(turnSpeed,0,0)

        elif bottom_right > threshold :
            zumi.control_motors(0,turnSpeed,0)
            
        elif bottom_right < threshold  and bottom_left < threshold:
            zumi.stop()
            screen.draw_text_center("Stop")
            break
            
except KeyboardInterrupt:
    zumi.stop()
    print("The interrupt button was pressed.")
      
try:
    screen.draw_text_center("Zumi Start")
    user_name = 'hsy'
    demo_name = 'BCcourse'

    knn = ColorClassifier(user_name=user_name)
    train = knn.load_model(demo_name)
    knn.fit("hsv")
    
    camera.start_camera()

    while True:    
            image = camera.capture()
            predict = knn.predict(image)
            screen.draw_text_center(predict)

            if predict == "red":
                zumi.stop()
            else:
                zumi.forward(0.5, 0.5)
                break               
finally:
    camera.close() 
    
try:
    threshold = 40
    turnSpeed = 1
    forwardSpeed = 1

    while True:   
        bottom_right = zumi.read_IR('bottom_right')
        bottom_left = zumi.read_IR('bottom_left')
        
        if bottom_left > threshold and bottom_right > threshold :      
            zumi.control_motors(forwardSpeed,forwardSpeed,0)

        elif bottom_left > threshold and bottom_right < threshold :
            zumi.control_motors(turnSpeed,0,0)

        elif bottom_left < threshold and bottom_right > threshold:
            zumi.control_motors(0,turnSpeed,0)

        elif bottom_left > threshold :
            zumi.control_motors(turnSpeed,0,0)

        elif bottom_right > threshold :
            zumi.control_motors(0,turnSpeed,0)
            
        elif bottom_right < threshold  and bottom_left < threshold:
            zumi.stop()
            screen.draw_text_center("Stop")
            break
            
except KeyboardInterrupt:
    zumi.stop()
    print("The interrupt button was pressed.")
      
try:
    screen.draw_text_center("Zumi Start")
    user_name = 'hsy'
    demo_name = 'BCcourse'

    knn = ColorClassifier(user_name=user_name)
    train = knn.load_model(demo_name)
    knn.fit("hsv")
    
    camera.start_camera()

    while True:    
            image = camera.capture()
            predict = knn.predict(image)
            screen.draw_text_center(predict)

            if predict == "red":
                zumi.stop()
            if predict == "green":
                zumi.forward(0.5, 0.5)
                break               
finally:
    camera.close()     
    

try:
    threshold = 40
    turnSpeed = 1
    forwardSpeed = 1

    while True:   
        bottom_right = zumi.read_IR('bottom_right')
        bottom_left = zumi.read_IR('bottom_left')
        
        if bottom_left > threshold and bottom_right > threshold :      
            zumi.control_motors(forwardSpeed,forwardSpeed,0)

        elif bottom_left > threshold and bottom_right < threshold :
            zumi.control_motors(turnSpeed,0,0)

        elif bottom_left < threshold and bottom_right > threshold:
            zumi.control_motors(0,turnSpeed,0)

        elif bottom_left > threshold :
            zumi.control_motors(turnSpeed,0,0)

        elif bottom_right > threshold :
            zumi.control_motors(0,turnSpeed,0)
            
        elif bottom_right < threshold  and bottom_left < threshold:
            zumi.stop()
            screen.draw_text_center("Stop")
            break
            
except KeyboardInterrupt:
    zumi.stop()
    print("The interrupt button was pressed.")


# In[6]:


#####line tracing

from zumi.zumi import Zumi
from zumi.util.camera import Camera
from zumi.util.screen import Screen
from zumi.util.color_classifier import ColorClassifier
import time

from threading import Thread
import IPython.display
import PIL.Image

camera = Camera()
screen = Screen()
zumi = Zumi()
from zumi.protocol import Note

try:
    threshold = 50
    turnSpeed = 1
    forwardSpeed = 1

    while True:   
        bottom_right = zumi.read_IR('bottom_right')
        bottom_left = zumi.read_IR('bottom_left')
        
        if bottom_left > threshold and bottom_right > threshold :      
            zumi.control_motors(forwardSpeed,forwardSpeed,0)

        elif bottom_left > threshold and bottom_right < threshold :
            zumi.control_motors(turnSpeed,0,0)

        elif bottom_left < threshold and bottom_right > threshold:
            zumi.control_motors(0,turnSpeed,0)

        elif bottom_left > threshold :
            zumi.control_motors(turnSpeed,0,0)

        elif bottom_right > threshold :
            zumi.control_motors(0,turnSpeed,0)
            
        elif bottom_right < threshold  and bottom_left < threshold:
            zumi.stop()
            screen.draw_text_center("Stop")
            break
            
except KeyboardInterrupt:
    zumi.stop()
    print("The interrupt button was pressed.")
    


# In[5]:


#QR

from zumi.util.camera import Camera
from zumi.util.vision import Vision

vision = Vision()
camera.start_camera()

try:
    for i in range(10):
        image = camera.capture()
        
        qr_code = vision.find_QR_code(image)
        
        message = vision.get_QR_message(qr_code)
        print(message)
        
        camera.show_image(image)
        camera.clear_output()
        
        index = 0
        result= 0

        for i in range (len(message)):
            if (message[i].isdigit()):
                index += 1
            else :
                if (message[i] == '+'):
                    result = int(message[0:index]) + int(message[index+1:len(message)])
                elif (message[i] == '-'):
                    result = int(message[0:index]) - int(message[index+1:len(message)])
                elif (message[i] == '*'):
                    result = int(message[0:index]) * int(message[index+1:len(message)])
                elif (message[i] == '/'):
                    result = int(message[0:index]) / int(message[index+1:len(message)])
        
        #짝수 왼쪽, 홀수 오른쪽
        
        #screen.draw_text_center(int(result))
        zumi.forward(4, 0.8)
    
        if (result % 2 == 0):
            zumi.turn_left()
        else:
            zumi.turn_right(100)
            zumi.forward(5)
        break
        
        
finally:
    camera.close()
    print("done")
    

try:
    threshold = 40
    turnSpeed = 1
    forwardSpeed = 1

    while True:   
        bottom_right = zumi.read_IR('bottom_right')
        bottom_left = zumi.read_IR('bottom_left')
        
        if bottom_left > threshold and bottom_right > threshold :      
            zumi.control_motors(forwardSpeed,forwardSpeed,0)

        elif bottom_left > threshold and bottom_right < threshold :
            zumi.control_motors(turnSpeed,0,0)

        elif bottom_left < threshold and bottom_right > threshold:
            zumi.control_motors(0,turnSpeed,0)

        elif bottom_left > threshold :
            zumi.control_motors(turnSpeed,0,0)

        elif bottom_right > threshold :
            zumi.control_motors(0,turnSpeed,0)
            
        elif bottom_right < 100  and bottom_left< 100:
            zumi.stop()
            screen.draw_text_center("Stop")
            break        
            
except KeyboardInterrupt:
    zumi.stop()
    print("The interrupt button was pressed.")


# In[7]:


#웃음

for i in range(3):
    screen.happy()
    time.sleep(0.5)
    zumi.forward(5, 0.1)
    zumi.reverse(5, 0.1)
    
    
#노래

zumi.play_note(Note.E4)
zumi.play_note(Note.D4)
zumi.play_note(Note.C4)
zumi.play_note(Note.D4)
zumi.play_note(Note.E4)
zumi.play_note(Note.E4)
zumi.play_note(Note.E4)
time.sleep(0.5)
zumi.play_note(Note.D4)
zumi.play_note(Note.D4)
zumi.play_note(Note.D4)
time.sleep(0.5)
zumi.play_note(Note.E4)
zumi.play_note(Note.G4)
zumi.play_note(Note.G4)
time.sleep(0.5)
zumi.play_note(Note.E4)
zumi.play_note(Note.D4)
zumi.play_note(Note.C4)
zumi.play_note(Note.D4)
zumi.play_note(Note.E4)
zumi.play_note(Note.E4)
zumi.play_note(Note.E4)
time.sleep(0.5)
zumi.play_note(Note.D4)
zumi.play_note(Note.D4)
zumi.play_note(Note.E4)
zumi.play_note(Note.D4)
zumi.play_note(Note.C4)

