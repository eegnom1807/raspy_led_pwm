import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

led = GPIO.PWM(7, 100)

led.start(0)
while True:
      led.ChangeDutyCycle(5)
