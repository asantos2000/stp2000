# Call it at /etc/rc.local
# Set any env vars before call it
# It
from gpiozero import Button
from signal import pause
import os

def pressed():
    print("Button pressed")
    os.system("python /home/pi/sendmail.py")

def released():
    print("Button released")

def power_pressed():
    print("Poweroff pressed")

def power_released():
    print("Powering off")
    os.system("sudo poweroff")

switch = Button(17)
poweroff = Button(27)

switch.when_pressed = pressed
switch.when_released = released

poweroff.when_pressed = power_pressed
poweroff.when_released = power_released

pause()