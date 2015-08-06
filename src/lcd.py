import time
import random
import math
import pyupm_i2clcd as lcd


def color(R, G, B):
    x = lcd.Jhd1313m1(0, 0x3E, 0x62)
    x.setColor(R, G, B)               

def color_water_heigh(water_height, water_max, water_warning):
    if water_height > 0.0 :
        color_semaphore(water_height / water_max, water_warning / water_max)

def color_semaphore(level, warning = 0.5):
    if level < 0.0 or 1.0 <= level :
        r = 255
        g = 0
        b = 0
    elif warning < 0.0 or 1.0 <= warning :
        r = 0
        g = 0
        b = 0
    elif level < warning:
        r = int((255 * (1.0 - (warning - level))))
        g = 255
        b = 0 
    else :
        r = 255
        g = int((255 * (1.0 - level + warning)))
        b = 0
    color(r, g ,b)

    
	
# This example will change the LCD backlight on the Grove-LCD RGB backlight
# to a nice shade of purple

c = 0.0

#while True:
    #R = random.randint(1, 255)
    #G = random.randint(1, 255)
    #B = random.randint(1, 255)
    #color(R,G,B)
    #color_semaphore(random.randint(0,100)/100)
    #c = 0.0
#    color_semaphore(c)
#    time.sleep(1)
#    c= c + 0.1


