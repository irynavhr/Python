# coding: cp1251

# ToDo: реалізуйте вихід з програми також при натисненні
#       ESC

import pygame as pg
import time

pg.init()
surface = pg.display.set_mode(size=(500,500),depth=32)

pg.event.clear()
pg.event.set_blocked(None)
pg.event.set_allowed(pg.KEYUP)

surface.fill((0,255,255))
pg.display.set_caption("Це гарний заголовок")
pg.display.update()

while True:
	event = pg.event.wait()
	print(event)
	# if CTRL + Q
	cntrl_q = (event.type == pg.KEYUP) and (event.scancode == 20) and \
	   (event.key == 113) and (event.mod == 4160)
	escp = (event.type == pg.KEYUP) and (event.scancode == 41) and \
	   (event.key == 27) and (event.mod == 4096)
	if cntrl_q or escp:
		print('Bye!!!')
		exit(0)
