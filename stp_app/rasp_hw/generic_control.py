import RPi.GPIO as GPIO
from flask import Flask, render_template, redirect, url_for

def change_gpio(changePin, action):
    # Convert the pin from the URL into an integer:
    pin = int(changePin)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    # Get the device name for the pin being changed:

    # If the action part of the URL is "on," execute the code indented below:
    if action == "on":
        # Set the pin high:
        GPIO.output(pin, GPIO.HIGH)
        # Save the status message to be passed into the template:
        message = "Turned " + changePin + " on."
    if action == "off":
        GPIO.output(pin, GPIO.LOW)
        message = "Turned " + changePin + " off."

    #GPIO.cleanup()

    return True
