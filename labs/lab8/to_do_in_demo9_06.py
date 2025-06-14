# coding: cp1251

# Гриценко Ірина Валеріївна
# ToDo: ��������� �������� ���� (�������������� ����� ��������)
#       ��� ���������� ���� ������ ����� ���������.

import pygame as pg
import time
import random as rnd

def processingEvents():
    while True:
        event = pg.event.wait()
        print(event)
        # if CTRL + Q
       
        if (event.type == pg.KEYUP) and (event.scancode == 20) and \
           (event.key == 113):
            print('Bye!!!')
            exit(0)
        elif (event.type == pg.KEYUP) and (event.scancode == 21) and \
           (event.key == 114):
            # print('red rectangle')
            r = pg.Rect(rnd.randint(10,250),rnd.randint(10,250),
                        rnd.randint(100,300),rnd.randint(100,300))
            pg.draw.rect(surface,(255,0,0),r,5)
            pg.display.update()
        elif (event.type == pg.KEYUP) and (event.scancode == 6) and \
           (event.key == 99):
            # print('cyan circle')
            c = (rnd.randint(10,490),rnd.randint(10,490))
            pg.draw.circle(surface,(200,200,255),c,20,5)
            pg.display.update()
        elif (event.type == pg.MOUSEBUTTONUP) and (event.button == 1):
            pos = event.pos
            r = pg.Rect(pos[0]-20,pos[1]-10,40,20)
            pg.draw.ellipse(surface,
                (rnd.randint(0,255),rnd.randint(0,255),rnd.randint(0,255)),
                r,3)
            pg.display.update()
        elif (event.type == pg.MOUSEBUTTONUP) and (event.button == 3):
            surface.fill((rnd.randint(0,255),rnd.randint(0,255),rnd.randint(0,255)))
            pg.display.update()

rnd.seed()

pg.init()
surface = pg.display.set_mode(size=(500,500),depth=32)

pg.event.clear()
pg.event.set_blocked(None)
pg.event.set_allowed([pg.KEYUP,pg.MOUSEBUTTONUP])

surface.fill((0,255,255))
pg.display.set_caption("�� ������ ���������")
pg.display.update()

processingEvents()
