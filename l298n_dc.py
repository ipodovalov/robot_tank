# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

import RPi.GPIO as GPIO
from time import sleep

from evdev import InputDevice, categorize, ecodes

gamepad = InputDevice('/dev/input/event0')

run_key = 19
forward_key = 103
backward_key = 108
stop_key = 28
low_key = 38
high_key = 35
middle_key = 50
exit_key = 18
left_key = 105
right_key = 106

# left front motor
in1 = 24
in2 = 23
en1 = 25

# right front motor
in3 = 27
in4 = 17
en2 = 22

# left back motor
in5 = 20
in6 = 16
en3 = 21

# right back motor
in7 = 13
in8 = 19
en4 = 26

temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(in5,GPIO.OUT)
GPIO.setup(in6,GPIO.OUT)
GPIO.setup(in7,GPIO.OUT)
GPIO.setup(in8,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.setup(en3,GPIO.OUT)
GPIO.setup(en4,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
GPIO.output(in5,GPIO.LOW)
GPIO.output(in6,GPIO.LOW)
GPIO.output(in7,GPIO.LOW)
GPIO.output(in8,GPIO.LOW)
p1=GPIO.PWM(en1,1000)
p2=GPIO.PWM(en2,1000)
p3=GPIO.PWM(en3,1000)
p4=GPIO.PWM(en4,1000)

p1.start(25)
p2.start(25)
p3.start(25)
p4.start(25)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")

for event in gamepad.read_loop():

    if event.type == ecodes.EV_KEY and event.value == 1:
        if event.code == run_key:
            print("run")
            if(temp1==1):
                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,GPIO.LOW)
                GPIO.output(in3,GPIO.HIGH)
                GPIO.output(in4,GPIO.LOW)
                GPIO.output(in5,GPIO.HIGH)
                GPIO.output(in6,GPIO.LOW)
                GPIO.output(in7,GPIO.HIGH)
                GPIO.output(in8,GPIO.LOW)
                print("forward")
                x='z'
            else:
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.HIGH)
                GPIO.output(in3,GPIO.LOW)
                GPIO.output(in4,GPIO.HIGH)
                GPIO.output(in5,GPIO.LOW)
                GPIO.output(in6,GPIO.HIGH)
                GPIO.output(in7,GPIO.LOW)
                GPIO.output(in8,GPIO.HIGH)
                print("backward")
                x='z'

        elif event.code == stop_key:
            print("stop")
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)
            GPIO.output(in5,GPIO.LOW)
            GPIO.output(in6,GPIO.LOW)
            GPIO.output(in7,GPIO.LOW)
            GPIO.output(in8,GPIO.LOW)
            x='z'

        elif event.code == forward_key:
            print("forward")
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in4,GPIO.LOW)
            GPIO.output(in5,GPIO.HIGH)
            GPIO.output(in6,GPIO.LOW)
            GPIO.output(in7,GPIO.HIGH)
            GPIO.output(in8,GPIO.LOW)
            temp1=1
            x='z'

        elif event.code == backward_key:
            print("backward")
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.HIGH)
            GPIO.output(in5,GPIO.LOW)
            GPIO.output(in6,GPIO.HIGH)
            GPIO.output(in7,GPIO.LOW)
            GPIO.output(in8,GPIO.HIGH)
            temp1=0
            x='z'

        elif event.code == low_key:
            print("low")
            p1.ChangeDutyCycle(25)
            p2.ChangeDutyCycle(25)
            p3.ChangeDutyCycle(25)
            p4.ChangeDutyCycle(25)
            x='z'

        elif event.code == right_key:
            print("Right key has been pushed by Pasha Podovalov")
            x='z'

        elif event.code == left_key:
            print("Left key has been pushed by Pasha Podovalov")
            x='z'

        elif event.code == middle_key:
            print("medium")
            p1.ChangeDutyCycle(50)
            p2.ChangeDutyCycle(50)
            p3.ChangeDutyCycle(50)
            p4.ChangeDutyCycle(50)
            x='z'

        elif event.code == high_key:
            print("high")
            p1.ChangeDutyCycle(75)
            p2.ChangeDutyCycle(75)
            p3.ChangeDutyCycle(75)
            p4.ChangeDutyCycle(75)
            x='z'

        elif event.code == exit_key:
            GPIO.cleanup()
            print("GPIO Clean up")
            break

        else:
            print("<<<  wrong data  >>>")
            print("please enter the defined data to continue.....")
