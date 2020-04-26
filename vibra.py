import RPi.GPIO as GPIO
from time import sleep

in1 = 24
in2 = 23
en = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.setup(en,GPIO.OUT)

p = GPIO.PWM(en, 1000)
p.start(25)

print("Activating motor 1")
GPIO.output(in1,GPIO.HIGH)
GPIO.output(in2,GPIO.LOW)
p.ChangeDutyCycle(25) # Low velocity

sleep(2)

print("Deactivating motor 1")
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

GPIO.cleanup()
