import RPi.GPIO as GPIO
import time

pins = [18, 17, 27, 22, 23, 24, 25, 12]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#set up pin outs in order of LED's
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

#set initial state to low
for pin in pins:
    GPIO.output(pin, 0)

while True:
    input = int(raw_input("Enter a number to be represented in binary (0 - 255): "))

    #display the proper bit
    for i in range(len(pins)):
        GPIO.output(pins[i], input & (1 << i))
    time.sleep(1)
