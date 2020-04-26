# Stop the Pigeon 2000

Inspiration: <https://youtu.be/sj6-LG5VpGk>

The STP2000 is a machine to stop pigeons to eat my neighbor's cat food.

![](media/20200412_170935.jpg)

![](media/20200412_163549.jpg)

Yes, it's a prototype, developed using raspberrypi 4, few sensors and actuators.

## Install services

Copy `stp_app.service` to `/lib/systemd/system`
Copy `buttons.service` to `/lib/systemd/system`
Copy  `override.conf` to `/etc/systemd/system/buttons.service.d`

```shell script
sudo systemctl daemon-reload

# Boot enable
sudo systemctl enable stp_app
sudo systemctl enable buttons

# Start / stop
sudo systemctl start stp_app
sudo systemctl start buttons

# Status
sudo systemctl status stp_app
sudo systemctl status buttons

# Log
journalctl -u stp_app -f
journalctl -u buttons -f
```

## References

* [How to Run a Raspberry Pi Program on Startup](https://learn.sparkfun.com/tutorials/how-to-run-a-raspberry-pi-program-on-startup#method-3-systemd)
* [How to set environment variable in systemd service?](https://serverfault.com/questions/413397/how-to-set-environment-variable-in-systemd-service)
* [What is the difference between BOARD and BCM for GPIO pin numbering?](https://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering)
* [Tutorial: Raspberry Pi GPIO Pins and Python](https://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/)
* [Python RPi.GPIO.add_event_detect() Examples](https://www.programcreek.com/python/example/98874/RPi.GPIO.add_event_detect)
* [Checking function of GPIO channels](https://sourceforge.net/p/raspberry-gpio-python/wiki/Checking%20function%20of%20GPIO%20channels/)
* [Absolute vs Relative Imports in Python](https://realpython.com/absolute-vs-relative-python-imports/)
* [sendgrid/sendgrid-python](https://github.com/sendgrid/sendgrid-python)
* [How to Send Emails in Python with Sendgrid](https://www.twilio.com/blog/how-to-send-emails-in-python-with-sendgrid)