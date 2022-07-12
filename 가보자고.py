from zumi.zumi import Zumi
from zumi.util.camera import Camera
from zumi.util.screen import Screen
from zumi.util.vision import Vision
from zumi.util.color_classifier import ColorClassifier
import time
from zumi.protocol import Note

camera = Camera()
screen = Screen()
zumi = Zumi()
vision = Vision()

//

#A코스
user_name = 'subin'
demo_name = 'oyb'
knn = ColorClassifier(user_name=user_name)
train = knn.load_model(demo_name)

zumi.play_note(Note.C4)
zumi.play_note(Note.D4)
zumi.play_note(Note.E4)

count = 0
answer = ""
correct = False

try:
    
    knn.fit("hsv")
    
    threshold = 100
    turnSpeed = 5
    forwardSpeed = 1
    
    while True:
        ir = zumi.get_all_IR_data()
        bottom_right_ir = ir[1]
        bottom_left_ir = ir[3]
        front_right = ir[0]
        front_left = ir[5]

        if bottom_left_ir > threshold and bottom_right_ir > threshold :
            zumi.control_motors(forwardSpeed,forwardSpeed,0)

        elif bottom_left_ir > threshold :
            zumi.control_motors(turnSpeed,0,0)

        elif bottom_right_ir > threshold :
            zumi.control_motors(0,turnSpeed,0)
        
        elif bottom_left_ir < threshold and bottom_right_ir < threshold :
            zumi.stop()
            
            if count==0 or count==2 :
                zumi.control_motors(forwardSpeed*1000,forwardSpeed*1000,0)
                zumi.control_motors(forwardSpeed*1000,forwardSpeed*1000,0)
                zumi.turn_right()
                zumi.forward(0.01)
                zumi.stop()
                count= count+1
                
            elif count==1 :
                zumi.stop()
                camera.start_camera()
                image = camera.capture()
                predict = knn.predict(image)
                #screen.draw_text_center(predict)
                print(predict)
                camera.show_image(image)
                camera.clear_output()
                
                if predict=='orange' :
                    screen.draw_text_center(predict)
                    zumi.turn_right()
                    zumi.turn_right()
                    count = count+1
                #왜 색깔 인식을 못헤............................
        

except KeyboardInterrupt:
    zumi.stop()
    camera.close()

//

#B코스
user_name = 'subin'
demo_name = 'rpg'
knn = ColorClassifier(user_name=user_name)
train = knn.load_model(demo_name)

zumi.play_note(Note.C4)
zumi.play_note(Note.D4)
zumi.play_note(Note.E4)

try:
    camera.start_camera()
    knn.fit("hsv")
    
    threshold = 100
    turnSpeed = 5
    forwardSpeed = 1
    
    while True:
        ir = zumi.get_all_IR_data()
        bottom_right_ir = ir[1]
        bottom_left_ir = ir[3]
        front_right = ir[0]
        front_left = ir[5]

        if bottom_left_ir > threshold and bottom_right_ir > threshold :
            zumi.control_motors(forwardSpeed,forwardSpeed,0)

        elif bottom_left_ir > threshold :
            zumi.control_motors(turnSpeed,0,0)

        elif bottom_right_ir > threshold :
            zumi.control_motors(0,turnSpeed,0)
        
        elif bottom_left_ir < threshold and bottom_right_ir < threshold :
            zumi.stop()
            
            if front_right < 150 and front_left < 150 :
                zumi.stop()
                image = camera.capture()

                predict = knn.predict(image)
                print(predict)
                screen.draw_text_center(predict)
                camera.show_image(image)
                camera.clear_output()

                if predict == "red":
                    zumi.stop()
                elif predict == "green":
                    zumi.control_motors(forwardSpeed*500,forwardSpeed*400,0)
                    
            else :
                zumi.control_motors(forwardSpeed*100,forwardSpeed*100,0)
                continue
                    
            
        

except KeyboardInterrupt:
    zumi.stop()
    camera.close()

//

#C코스

user_name = 'subin'
demo_name = 'rpg'
knn = ColorClassifier(user_name=user_name)
train = knn.load_model(demo_name)

try:
    camera.start_camera()
    knn.fit("hsv")
    
    threshold = 100
    turnSpeed = 5
    forwardSpeed = 1
    
    check = False
    
    while True:
        ir = zumi.get_all_IR_data()
        bottom_right_ir = ir[1]
        bottom_left_ir = ir[3]
        front_right = ir[0]
        front_left = ir[5]
            
                    
        if bottom_left_ir > threshold and bottom_right_ir > threshold :
            zumi.control_motors(forwardSpeed,forwardSpeed,0)

        elif bottom_left_ir > threshold :
            zumi.control_motors(turnSpeed,0,0)

        elif bottom_right_ir > threshold :
            zumi.control_motors(0,turnSpeed,0)
        
        elif bottom_left_ir < threshold and bottom_right_ir < threshold :
            zumi.stop()
            
            if check == False:
                while True:
                    image = camera.capture()

                    qr_code = vision.find_QR_code(image)

                    print("center : " , vision.get_QR_center(qr_code))
                    print("dimensions : " , vision.get_QR_dimensions(qr_code))                
                    print("message : " , vision.get_QR_message(qr_code))
                    print("polygon : " , vision.get_QR_polygon(qr_code))

                    message = vision.get_QR_message(qr_code)
                    
                    if message == None :
                        continue
                        
                    else:
                        p = eval(message)
                        print(p)
                        camera.show_image(image)
                        camera.clear_output()

                        if p%2==0:
                            zumi.forward(25)
                            zumi.turn_left()
                            check = True
                            break
                        else:
                            zumi.forward(30)
                            zumi.turn_right()
                            check = True
                            break
            else:
                zumi.stop()
                image = camera.capture()

                predict = knn.predict(image)
                print(predict)
                screen.draw_text_center(predict)
                camera.show_image(image)
                camera.clear_output()

                if predict == "purple":
                    
                    screen.happy()
                    for i in range(3):
                        zumi.turn_left(180)
                        zumi.turn_right(180)
                        # 찐막 춤추기~~~~~~
                    break

            
finally:
    camera.close()
    print("done")
