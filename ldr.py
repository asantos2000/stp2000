from gpiozero import LightSensor
from signal import pause
import logging
from datetime import datetime
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

def sundown(msg):
    logging.info("LDR: It is sundown!")
    logging.info(f'ldr value: {ldr.value}')

def sunrise():
    logging.info("LDR: It is sunrise!")
    logging.info(f'ldr value: {ldr.value}')

logging.info("LDR program started.")

ldr = LightSensor(16)
logging.info(f'ldr value: {ldr.value}')
#ldr.wait_for_light()
#print("Light detected!")

ldr.when_dark = sundown
ldr.when_light = sunrise

pause()