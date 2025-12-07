import RPi.GPIO as GPIO
import os
#import time
#import math
print(GPIO.RPI_INFO)
# Set up GPIO mode
for dev in ['/dev/gpiomem', '/dev/gpiomem0', '/dev/mem']:
    print(f"{dev}: {'exists' if os.path.exists(dev) else 'missing'}")
#GPIO.setmode(GPIO.BOARD)

GPIO.RPI_INFO['P1_REVISION'] = 3  # or 2 or 1 depending on your Pi
GPIO.setmode(GPIO.BCM)
# Motor 1 Pins

#EN1_PIN = 25  # Use a PWM pin
M1_PWM1_PIN = 12   
M1_PWM2_PIN = 22

M2_PWM1_PIN = 8   
M2_PWM2_PIN = 10

#EN1_PIN = 22  # Use a PWM pin
#PWM1_PIN = 18   
#PWM2_PIN = 25

# Setup GPIO pins
GPIO.setup(M1_PWM1_PIN, GPIO.OUT)
GPIO.setup(M1_PWM2_PIN, GPIO.OUT)

GPIO.setup(M2_PWM1_PIN, GPIO.OUT)
GPIO.setup(M2_PWM2_PIN, GPIO.OUT)

# Set up PWM on the pins with a frequency of 1000Hz
pwm1_motor1 = GPIO.PWM(M1_PWM1_PIN, 1000)
pwm2_motor1 = GPIO.PWM(M1_PWM2_PIN, 1000)

pwm1_motor2 = GPIO.PWM(M2_PWM1_PIN, 1000)
pwm2_motor2 = GPIO.PWM(M2_PWM2_PIN, 1000)

# Start PWM with 0 duty cycle (motors stopped)
pwm1_motor1.start(0)
pwm2_motor1.start(0)

pwm1_motor2.start(0)
pwm2_motor2.start(0)

# Function to control motor direction and speed
def control_motor(motor_num, speed):
    if motor_num == 1:
        if speed > 0:
            print("FORWARD")
            pwm1_motor1.ChangeDutyCycle(abs(speed))       # Speed is between 0-100%
            pwm2_motor1.ChangeDutyCycle(0)       # Speed is between 0-100%

        elif speed < 0:
            print("Reverse")
            pwm1_motor1.ChangeDutyCycle(0)       # Speed is between 0-100%
            pwm2_motor1.ChangeDutyCycle(abs(speed))       # Speed is between 0-100%
            print("FORWARD")
        else:
            pwm1_motor1.ChangeDutyCycle(0)       # Speed is between 0-100%
            pwm2_motor1.ChangeDutyCycle(0)       # Speed is between 0-100%

    if motor_num == 2:
        if speed < 0:
            print("FORWARD")
            pwm1_motor2.ChangeDutyCycle(abs(speed))       # Speed is between 0-100%
            pwm2_motor2.ChangeDutyCycle(0)       # Speed is between 0-100%

        elif speed > 0:
            print("Reverse")
            pwm1_motor2.ChangeDutyCycle(0)       # Speed is between 0-100%
            pwm2_motor2.ChangeDutyCycle(abs(speed))       # Speed is between 0-100%
            print("FORWARD")
        else:
            pwm1_motor2.ChangeDutyCycle(0)       # Speed is between 0-100%
            pwm2_motor2.ChangeDutyCycle(0)       # Speed is between 0-100%

