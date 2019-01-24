import RPi.GPIO as GPIO
import time

#set up pin outs in order of LED's
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setwarnings(False)

#set initial state to low
GPIO.output(18, 0)
GPIO.output(17, 0)
GPIO.output(27, 0)
GPIO.output(22, 0)
GPIO.output(23, 0)
GPIO.output(24, 0)
GPIO.output(25, 0)
GPIO.output(12, 0)

while True:
    input = int(raw_input("Enter a number to be represented in binary (0 - 255): "))

    #display the proper bit
    GPIO.output(18, input & 0b1) #2^0
    GPIO.output(17, input & 0b10) #2^1
    GPIO.output(27, input & 0b100) #2^2
    GPIO.output(22, input & 0b1000) #2^3
    GPIO.output(23, input & 0b10000) #2^4
    GPIO.output(24, input & 0b100000) #2^5
    GPIO.output(25, input & 0b1000000) #2^6
    GPIO.output(12, input & 0b10000000) #2^7
    time.sleep(1)
