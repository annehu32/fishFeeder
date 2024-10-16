import time
from machine import Pin, PWM

servo = PWM(Pin('GPIO6',Pin.OUT))
servo.freq(50)

button = Pin('GPIO8', Pin.IN, Pin.PULL_UP)
isMoving = False

minPWM = 1802
maxPWM = 7654
midPWM = int(maxPWM/2)

def moveServo():
    print("moving to min PWM")
    servo.duty_u16(minPWM)
    time.sleep(2)
    print("at min PWM")
    
    print("moving to mid PWM")
    servo.duty_u16(midPWM)
    time.sleep(2)
    print("at mid PWM")

    print("moving to max PWM")
    servo.duty_u16(minPWM)
    time.sleep(2)
    print("at mid PWM")
    
    for i in range(0,10):
        print("sleeping..... : "+str(i))
        time.sleep(1)
        
try:
    while True:
        if button.value() is 0 and not isMoving:
            isMoving = True
            moveServo()
            isMoving = False
            
            
except KeyboardInterrupt:
    print("keyboard interrupt")
    servo.deinit()
