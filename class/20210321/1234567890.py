from microbit import *
compass.calibrate()
while True:
    h = compass.heading()
    if h <= 46:
        display.show('N')
    elif h <=
        display.show(' ')