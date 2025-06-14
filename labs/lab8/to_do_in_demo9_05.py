# coding: cp1251

# ToDo: додайте рисування горизонтальної лінії через усе вікно
#       при натисненні "H", вертикальної лінії через усі вікно
#       при натисненні "Alt + V", похилої лінії при натисненні
#       "Ctrl + Alt + D". Колір та координати вибираються
#       випадковим чином.

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
            r = pg.Rect(rnd.randint(10,100),rnd.randint(10,50),
                        rnd.randint(100,300),rnd.randint(100,300))
            pg.draw.rect(surface,(255,0,0),r,5)
            # r = pg.Rect(50,50,100,200)
            # pg.draw.rect(surface,(255,255,255),r,10)
            pg.display.update()
        elif (event.type == pg.KEYUP) and (event.scancode == 6) and \
           (event.key == 99) :
            # print('cyan circle')
            c = (rnd.randint(10,200),rnd.randint(10,200))
            pg.draw.circle(surface,(200,200,255),c,20,5)
            pg.display.update()
            # if H:
        elif (event.type == pg.KEYUP) and (event.scancode == 11) and \
           (event.key == 104):
            rnd_x_line = rnd.randint(0, 500)
            pg.draw.line(surface, (rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255)), (rnd_x_line, 0), (rnd_x_line, 500), 2)
            pg.display.update()
        # "Alt + V"
        elif (event.type == pg.KEYUP) and (event.scancode == 25) and \
           (event.key == 118):
            rnd_y_line = rnd.randint(0, 500)
            pg.draw.line(surface, (rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255)), (0, rnd_y_line), (500, rnd_y_line), 2)
            pg.display.update()
        # "Ctrl + Alt + D"
        elif (event.type == pg.KEYUP) and (event.scancode == 7) and \
           (event.key == 100):
            c = (rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255))
            gen = rnd.randint(0, 1)
            if gen == 0:
                start = (0, rnd.randint(0, 500))
                finish =(500, rnd.randint(0, 500))
            else:
                start = (rnd.randint(0, 500), 0)
                finish =(rnd.randint(0, 500),500)

            pg.draw.line(surface, c, start, finish, 3)
            pg.display.update()


rnd.seed()

pg.init()
surface = pg.display.set_mode(size=(500,500),depth=32)

pg.event.clear()
pg.event.set_blocked(None)
pg.event.set_allowed(pg.KEYUP)

surface.fill((0,255,255))
pg.display.set_caption("Це гарний заголовок")
pg.display.update()

processingEvents()
