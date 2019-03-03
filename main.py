import RPi.GPIO as gpio
from time import sleep
from wave import Distance # 초음파 거리 계산
from moter import Rotation # 모터를 이용한 회전
from picamera import PiCamera # 카메라 사용
from mysql import mysql_execute # 쿼리 전송

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

camera = PiCamera()
camera.resolution = (800, 400) # 카메라 해상도 설정
camera.brightness = 60 # 카메라 밝기 설정

trig = 13
echo = 19
moterPin = 18
temp = None
print("Start")

i = 1
while(1):
    Rotation(moterPin, 2.5)
    if Distance(trig, echo) < 200:
        sleep(5)
        if Distance(trig, echo) < 200:
            temp = True
            camera.start_preview()
            sleep(3)
            mysql_execute("P1", True)
            camera.capture("test.jpg")
            camera.stop_preview()
    elif Distance(trig, echo) >= 50 and temp == True:
        temp = False
        mysql_execute("P1", False)

    sleep(5)

    Rotation(moterPin, 5.2)
    if Distance(trig, echo) < 150:
        sleep(5)
        if Distance(trig, echo) < 150:
            temp = True
            camera.start_preview()
            sleep(3)
            mysql_execute("P2", True)
            camera.capture("test.jpg")
            camera.stop_preview()
    elif Distance(trig, echo) >= 50 and temp == True:
        temp = False
        mysql_execute("P2", False)

    sleep(5)

    Rotation(moterPin, 8.7)
    if Distance(trig, echo) < 200:
        sleep(5)
        if Distance(trig, echo) < 200:
            temp = True
            camera.start_preview()
            sleep(3)
            mysql_execute("P3", True)
            camera.capture("test.jpg")
            camera.stop_preview()
    elif Distance(trig, echo) >= 50 and temp == True:
        temp = False
        mysql_execute("P3", False)

    sleep(10)
