#!/usr/bin/python
# coding: utf-8

try:
    from sense_hat import SenseHat
    sense = SenseHat()
except:
    from sense_emu import SenseHat
    sense = SenseHat()

import time
#sense = SenseHat()
sense.clear();

raquette=(0,0,255)
balle=(255,255,255)
noir=(0,0,0)
x = 0
y = 0

#affichage raquette bleu au bord (x, y, r, g, b)
sense.set_pixel(0, 0, raquette)
sense.set_pixel(0, 1, raquette)
sense.set_pixel(0, 2, raquette)

#affichage balle blanche au centre (x, y, r, g, b)
sense.set_pixel(x, y, balle)

while 1:
    sense.set_pixel(x, y, noir)
    x += 1
    if x >= 8:
        break
    y += 1
    if y >= 8:
        break
    sense.set_pixel(x, y, balle)
    time.sleep(0.2)    
from sense_hat import SenseHat
import time
sense = SenseHat()
sense.clear();

raquette=(0,0,255)
balle=(255,255,255)
noir=(0,0,0)
x = 3 
y = 7
depx = 1
depy = 1

#affichage raquette bleu au bord (x, y, r, g, b)
sense.set_pixel(0, 0, raquette)
sense.set_pixel(0, 1, raquette)
sense.set_pixel(0, 2, raquette)

#affichage balle blanche au centre (x, y, r, g, b)
sense.set_pixel(x, y, balle)

while 1:
    sense.set_pixel(x, y, noir)
    x -= depx
    if x == 0 or x == 7:
        depx *= -1
    y -= depy
    if y == 0 or y == 7:
        depy *= -1
    sense.set_pixel(x, y, balle)
    time.sleep(0.2)    

from sense_emu import SenseHat
import time
sense = SenseHat()
sense.clear();

raquette=(0,0,255)
balle=(255,255,255)
noir=(0,0,0)
x = 3 
y = 7
z = 4
depx = 1
depy = 1

#affichage raquette bleu au bord (x, y, r, g, b)
sense.set_pixel(0, z+0, raquette)
sense.set_pixel(0, z+1, raquette)
sense.set_pixel(0, z+2, raquette)

#affichage balle blanche au centre (x, y, r, g, b)
sense.set_pixel(x, y, balle)

while 1:
    sense.set_pixel(x, y, noir)
    x -= depx
    if x == 0 or x == 7:
        depx *= -1
    y -= depy
    if y == 0 or y == 7:
        depy *= -1
    sense.set_pixel(x, y, balle)
    time.sleep(0.2)    

