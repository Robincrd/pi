import RPi.GPIO as GPIO
import time

# Pin of servos 
# You can connect servos to I/O pins including 7, 11, 12, 13, 15, 16, 18, 22
servoPIN1 = 11

# Set numbering mode (BOARD/BCM)
# BOARD (le plus logique):
#   ------
#  | 1  2 |
#  | 3  4 |
#  | 5  6 |
#  : :  : : 
GPIO.setmode(GPIO.BOARD) 

# Set servoPIN1 as an output
GPIO.setup(servoPIN1, GPIO.OUT)

# Set servos as servosPINs as PWM, 50Hz pulse
servo1 = GPIO.PWM(servoPIN1, 50)

# Start PWN running, with value of 0 (pulse off)
servo1.start(0)

time.sleep(1)

# Calcul de l'angle
angle = 45 
angle = 2+(angle/18)       # 2 <= angle <= 12
                            
# Loop for duty values from 2 to 12 (0 to 180 degrees)
# Mouvement / Arrêt (pour empêcher la "convulsion")
while angle <= 12:
    servo1.ChangeDutyCycle(angle)       # Mouvement
    time.sleep(0.3)
    servo1.ChangeDutyCycle(0)           # Arrêt
    time.sleep(0.7)
    angle = angle + 1

# Cleaning
servo1.stop()
GPIO.cleanup()