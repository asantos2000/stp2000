from gpiozero import LED
from time import sleep

ima = LED(16)

while True:
    print("magneto on")
    ima.on()
    sleep(2)
    print("magneto off")
    ima.off()
    sleep(4)