import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

led = GPIO.PWM(7, 100)

led.start(0)
while True:
   led.start(0)
   for i in range(0, 100, 25):
      print(i)
      led.ChangeDutyCycle(i)
      time.sleep(0.5)
