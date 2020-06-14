from gpiozero import LightSensor
import logging
from time import sleep

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

ldr = LightSensor(16)  # alter if using a different pin

while True:
    logging.info('ldr value: {}'.format(ldr.value))
    sleep(5)