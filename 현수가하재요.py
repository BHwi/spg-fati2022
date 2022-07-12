
import time
import IPython.display
from zumi.util.camera import Camera
from zumi.util.color_classifier import ColorClassifier
from zumi.zumi import Zumi
from zumi.util.screen import Screen
from zumi.protocol import Note
from zumi.util.vision import Vision

zumi = Zumi()
screen = Screen()
camera = Camera()

user_name = 'test'
parking = 'zumilove'
light = 'redgreen'
parking_knn = ColorClassifier(user_name=user_name)
light_knn = ColorClassifier(user_name=user_name)

threshold = 100
turnSpeed = 1
forwardSpeed = 1

# 시간 변수
t = 3

# 신호음
def music() :
    zumi.play_note(Note.C4)
    zumi.play_note(Note.D4)
    zumi.play_note(Note.E4)
    
# 속도 변화
def changeSpeed(ts, fs) :
    global turnSpeed, fowardSpeed
    
    turnSpeed = ts
    fowardSpeed = fs


# 바닥 확인 변수
bottom_right = zumi.read_IR('bottom_right')
bottom_left = zumi.read_IR('bottom_left')


# 저장 이미지 변수
find_image = None

# Zumi 학습
def knn() :
    train = parking_knn.load_model(parking)
    parking_knn.fit("hsv")
    train = light_knn.load_model(light)
    light_knn.fit("hsv")

# 바닥 아래 색이 하얀색일 경우 True 반환
def isWhite() :
    if bottom_right < threshold and bottom_left < threshold :
        return True
    else :
        return False

# bottom 감지기 읽기
def bottom_read() :
    global bottom_right, bottom_left
    bottom_right = zumi.read_IR('bottom_right')
    bottom_left = zumi.read_IR('bottom_left')
    
# 라인 트레이싱
def lane_trace() :
    bottom_read() 

    if bottom_left < threshold and bottom_right > threshold :
        zumi.stop()
        zumi.control_motors(0,turnSpeed,0)
    elif bottom_left > threshold and bottom_right < threshold :
        zumi.stop()
        zumi.control_motors(turnSpeed,0,0)
    else :
        zumi.control_motors(forwardSpeed,forwardSpeed,0)
        
# 갈림길에서 멈추는 함수
def cross_road_stop() :
    while isWhite() :
        lane_trace()
        bottom_read()
    
    zumi.stop()

# 이미지 로드 return : 이미지 이름
def image_load(name) :
    camera.start_camera() 
    
    if name == "parking" :
        image = camera.capture()
        ret = parking_knn.predict(image)
    else :
        image = camera.capture()
        ret = light_knn.predict(image)
        
    # screen.draw_text(ret)
    camera.close()
    return ret
    
# 주차 공간이 맞는지 확인하는 함수
def turn(stop_count) :
    ret = False;
    
    if stop_count % 2 == 0 :
        zumi.turn_right()
    else :
        zumi.turn_left()
    
    while not isWhite() :
        lane_trace()
        bottom_read()
    
    zumi.stop()
    
    image = image_load("parking")
#     if stop_count == 0 : 
#         image = 'orange'
#     if stop_count == 1 : 
#         image = 'yellow'
#     if stop_count == 2 : 
#         image = 'blue'
    
    if image == find_image :
        zumi.stop()
        time.sleep(1)
        ret = True
    
    zumi.stop()
    zumi.turn_left(180)
    
    while True :
        lane_trace()
        bottom_read()
        
        if isWhite() :
            break
    
    zumi.stop()
    
    if stop_count % 2 == 0 :
        zumi.smooth_turn_right(45, 2, 2)
    else :
        zumi.smooth_turn_left(45, 2, 2)
    
    lane_trace()
        
    return ret
    
# returnQRcode
def returnQRcode() :
    global camera
    vision = Vision()
    camera.start_camera()
    
    while True :
        image = camera.capture()
        qr_code = vision.find_QR_code(image)
        camera.show_image(image)
        
        if qr_code:
            camera.clear_output()
            camera.close()
            strData = vision.get_QR_message(qr_code)
            ans = eval(strData)
            return ans
        
def start() :
    while isWhite():
        lane_trace()
        bottom_read()
    
    lane_trace()

def acourse() :
    start()
    try:
        global find_image
        find = False
        stop_count = 0
        
        while True:
            if stop_count == 3 :
                zumi.stop()
                break
            
            lane_trace()
            bottom_read()
            
            if isWhite() :
                cross_road_stop()
                
                if stop_count == 0 :
                    time.sleep(3)
                    find_image = image_load("parking")
                
                if not find :
                    if turn(stop_count) :
                        find = True
                    stop_count += 1
            
            
    except KeyboardInterrupt:
        zumi.stop()
        print("The interrupt button was pressed.")
        
def bcourse() :
    try:
        stop_count = 0
        
        while True:
            if stop_count == 2 :
                break
            lane_trace()
            bottom_read()
            
            if isWhite() :
                zumi.stop()
                time.sleep(2)
                image = image_load("light")
                
                while image == "red" :
                    # screen.draw_text(image)
                    image = image_load("light")
                    
                stop_count += 1
                
                while isWhite() :
                    lane_trace()
            
    except KeyboardInterrupt:
        zumi.stop()
        print("The interrupt button was pressed.")

def ccourse():
    while True:
        lane_trace()
        if isWhite() :
            zumi.stop()
            break
    
    flag = returnQRcode()
    screen.draw_text_center(str(flag))
    
    while isWhite():
        lane_trace()
        bottom_read()
        
    while not isWhite():
        lane_trace()
        bottom_read()
    
    if flag % 2 == 0 :
        zumi.turn_left(80)
    else :
        zumi.turn_right(115, 2)
        
    while True:
        lane_trace()
        bottom_read()
        
        if isWhite() :
            break
    
    zumi.stop()

def dance() :
    zumi.turn_left()
    
    for i in range(0, 2) :
        zumi.turn_right(180)
        zumi.turn_left(180)
        
    zumi.turn_right()
    
def emotion() :
    for i in range(0, 4) :

        screen.draw_text_center("^ ___ ^", font_size = 25)

        time.sleep(1)

        screen.draw_text_center("^  O  ^", font_size = 25)

        time.sleep(1)
    
    screen.draw_text(" ")
    
knn()
music()
acourse()
bcourse()
ccourse()
dance()
emotion()