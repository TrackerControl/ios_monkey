from zxtouch.client import zxtouch
from zxtouch.toasttypes import *
import time
from zxtouch.touchtypes import *
from random import randrange
import random, string

device = zxtouch("127.0.0.1")

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

dims = device.get_screen_size()[1]
w = int(dims['width'].split(".")[0])
h = int(dims['height'].split(".")[0])

def move(startx,starty,endx,endy):
	device.touch(TOUCH_DOWN, 1, startx, starty)
	time.sleep(0.1)
	device.touch(TOUCH_MOVE, 1, endx, endy)
	time.sleep(0.5)
	device.touch(TOUCH_UP, 1, endx, endy)
	time.sleep(0.1)

def randommove():
	startx = randrange(w)
	starty = randrange(w)
	endx = startx + (randrange(100) * (-1 * randrange(2)))
	endy = starty + (randrange(100) * (-1 * randrange(2)))
	move(startx,starty,endx,endy)

def touch(x,y):
	device.touch(TOUCH_DOWN, 1, x, y)
	time.sleep(0.1)
	device.touch(TOUCH_UP, 1, x, y)
	time.sleep(0.1)

def randomtouch():
	startx = randrange(w)
	starty = randrange(w)
	touch(startx, starty)

def presscorners():
	base = randrange(100)
	if randrange(4) == 1:
		touch(base,base)
	if randrange(4) == 1:
		touch(w-base,h-base)
	if randrange(4) == 1:
		touch(base,h-base)
	if randrange(4) == 1:
		touch(w-base,base)

# run for ten minutes max -- this serves as a backup; the script should be quit earlier
t_end = time.time() + 60 * 10
while time.time() < t_end:
#for x in range(10):
#	print(x)
	if randrange(5) == 1:
		device.hide_keyboard()
		time.sleep(0.1)
	randommove()
	randomtouch()
	presscorners()
	if randrange(5) == 1:
		device.show_keyboard()
		time.sleep(0.1)
	time.sleep(0.5)
	device.insert_text(randomword(5))
	time.sleep(0.1)

device.disconnect()