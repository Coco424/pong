from sense_hat import SenseHat
import time
sense = SenseHat()
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
