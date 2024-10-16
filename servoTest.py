import time
from machine import Pin, PWM

servo = PWM(Pin('GPIO6',Pin.OUT))
servo.freq(50)

minPWM = 1802
maxPWM = 7654
midPWM = int(maxPWM/2)

try:
    while True:
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

except KeyboardInterrupt:
    print("keyboard interrupt")
    servo.deinit()
