import RPi.GPIO as GPIO
from flask import Flask, render_template, request
def status_report():
    GPIO.setmode(GPIO.BCM)

    # Create a dictionary called pins to store the pin number, name, and pin state:
    pins = {
        10: {'name': 'GPIO 10', 'state': GPIO.LOW},
        11: {'name': 'GPIO 11', 'state': GPIO.LOW},
        12: {'name': 'GPIO 12', 'state': GPIO.LOW},
        13: {'name': 'GPIO 13', 'state': GPIO.LOW},
        14: {'name': 'GPIO 14', 'state': GPIO.LOW},
        15: {'name': 'GPIO 15', 'state': GPIO.LOW},
        16: {'name': 'GPIO 16', 'state': GPIO.LOW},
        17: {'name': 'GPIO 17', 'state': GPIO.LOW},
        18: {'name': 'GPIO 18', 'state': GPIO.LOW},
        19: {'name': 'GPIO 19', 'state': GPIO.LOW},
        20: {'name': 'GPIO 20', 'state': GPIO.LOW},
        21: {'name': 'GPIO 21', 'state': GPIO.LOW},
        22: {'name': 'GPIO 22', 'state': GPIO.LOW},
        23: {'name': 'GPIO 23', 'state': GPIO.LOW},
        24: {'name': 'GPIO 24', 'state': GPIO.LOW}
    }

    # Set each pin as an output and make it low:
    for pin in pins:
        func = GPIO.gpio_function(pin)
        GPIO.setup(pin, func)
        # For each pin, read the pin state and store it in the pins dictionary:
        pins[pin]['state'] = GPIO.input(pin)

    # Along with the pin dictionary, put the message into the template data dictionary:
    templateData = {
        'pins': pins
    }

    #GPIO.cleanup()

    return render_template('status.html', **templateData)
