import RPi.GPIO as GPIO
import time

# Set numbering mode (BOARD/BCM)
GPIO.setmode(GPIO.BOARD) 

# I/O pins for servos : 7, 11, 12, 13, 15, 16, 18, 22
servoPIN1 = 11
servoPIN2 = 12

# Set servoPINs as outputs
GPIO.setup(servoPIN1, GPIO.OUT)
GPIO.setup(servoPIN2, GPIO.OUT)

# Set servos as servosPINs as PWM, 50Hz pulse
servo1 = GPIO.PWM(servoPIN1, 50)
servo2 = GPIO.PWM(servoPIN2, 50)

# Start PWN running with pulse off
servo1.start(0)
servo2.start(0)

time.sleep(1)

# Calcul des angles
angle1 = 0
angle1 = 2+(angle1/18)

angle2 = 180
angle2 = 2+(angle2/18)
                            
# Loop for duty values from 2 to 12 (0 to 180 degrees)
while angle1 <= 12:
    servo1.ChangeDutyCycle(angle1)
    servo2.ChangeDutyCycle(angle2)
    time.sleep(0.3)
    servo1.ChangeDutyCycle(0)
    servo2.ChangeDutyCycle(0)
    time.sleep(0.7)
    angle1 = angle1 + 1
    angle2 = angle2 - 1

# Cleaning
servo1.stop()
servo2.stop()
GPIO.cleanup()