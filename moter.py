import RPi.GPIO as gpio
import time

def Rotation(pin, angle) :
    gpio.setup(pin, gpio.OUT)
    p = gpio.PWM(pin, 50)
    p.start(0)

    p.ChangeDutyCycle(angle)
    print "angle :", angle
    time.sleep(1)

    p.stop()
