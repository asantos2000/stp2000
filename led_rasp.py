import RPi.GPIO as GPIO          
from time import sleep

in1 = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
for a in range(1, 11):
  print("blink {}".format(a))
  GPIO.output(in1,GPIO.HIGH)
  sleep(2)
  GPIO.output(in1,GPIO.LOW)
  sleep(2)

GPIO.cleanup()
    
