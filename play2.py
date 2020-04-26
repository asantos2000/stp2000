#!/usr/bin/env python
import os, random

def rndmp3 ():
    randomfile = random.choice(os.listdir("/home/pi/birds/"))
    file = ' /home/pi/birds/'+ randomfile
    #os.system ('mplayer' + file)
    os.system ('omxplayer -o local ' + file)

rndmp3 ()
