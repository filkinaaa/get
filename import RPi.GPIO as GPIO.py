import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [24, 25, 8, 7, 12, 16, 20, 21]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       

GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)
while True:
    for i in range(8):
        GPIO.output(leds[i], 1)
        time.sleep(1)
        GPIO.output(leds[i], 0)
