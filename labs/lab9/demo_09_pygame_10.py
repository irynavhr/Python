# coding: cp1251

# Гриценко Ірина Валеріївна
# ToDo: 
# 1. Додайте можливість переміщення ліній за курсором мишки
#       лише при включеному відповідному режимі.
# 2. При виключеному режимі з п. 1 у заголовку вікна повинні відображуватись
#       поточні координати курсора мишки.

import pygame as pg
import time

global x, y
x = 0
y = 0
maxx = 500
maxy = 500

# initialisation of graphics
# input: title - window title
# output: surface (graphics context)
def initGraphics(title):
    global x, y
    pg.init()

    bits = 32
    surface = pg.display.set_mode((maxx,maxy),0,bits)
    surface.fill((0,0,0))

    grid(surface)

    pg.event.set_blocked(None)
    pg.event.clear()
    pg.event.set_allowed([pg.KEYUP,pg.MOUSEBUTTONUP,pg.MOUSEMOTION])

    pg.display.set_caption(f'show lines: {flagShowText}, x = {x}, y = {y}')
    pg.display.update()

    return surface

# waiting and input processing
def waiting( surface ):
    global flagShowText
    # global playing
    while True:
        global event 
        event = pg.event.wait()
        # if space
        if (event.type == pg.KEYUP) and (event.scancode == 44) and (event.key == 32):
            surface.blit(surfaceReserve,(0,0))
            pg.display.update()
        # if escape
        elif (event.type == pg.KEYUP) and (event.scancode == 41) and (event.key == 27):
            pg.quit()
            exit(0)
                # if 't'
        elif (event.type == pg.KEYUP) and (event.scancode == 23) and \
           (event.key == 116):
            flagShowText = not flagShowText
            # print(flagShowText)
            pg.display.set_caption(f'show lines: {flagShowText}, x = {x}, y = {y}')
            pg.display.update()
        elif (event.type == pg.KEYUP):
            print(event.type)
            print(event.scancode)
            print(event.key)
        elif (event.type == pg.MOUSEBUTTONUP):
            
            # surface.fill((0,0,0))
            # grid( surface )
            surface.blit(surfaceReserve,(0,0))
            pg.draw.line(surface,(200,255,200),(0,event.pos[1]),(maxx,event.pos[1]))
            pg.draw.line(surface,(200,255,200),(event.pos[0],0),(event.pos[0],maxy))
            pg.draw.circle(surface,(0,255,0),(event.pos[0],event.pos[1]),3)
            pg.display.update()
        elif (event.type == pg.MOUSEMOTION):
            x = event.pos[0]
            y = event.pos[1]
            pg.display.set_caption(f'show lines: {flagShowText}, x = {x}, y = {y}')
            if flagShowText:
                surface.blit(surfaceReserve,(0,0))
                pg.draw.line(surface,(200,255,200),(0,event.pos[1]),(maxx,event.pos[1]))
                pg.draw.line(surface,(200,255,200),(event.pos[0],0),(event.pos[0],maxy))
                pg.draw.circle(surface,(0,255,0),(event.pos[0],event.pos[1]),3)
                pg.display.update()

# draw grid
# input: surface
def grid(surface):
    for i in range(100,maxx,100):
        pg.draw.line(surface,(100,100,100),(i,0),(i,maxy))
    for i in range(100,maxy,100):
        pg.draw.line(surface,(100,100,100),(0,i),(maxx,i))

global flagShowText
flagShowText = False

surface = initGraphics( "Test example" )
pg.display.update()
surfaceReserve = surface.copy()

# pg.draw.circle(surface,(255,255,0),(250,250),100)
# pg.display.update()

myfont = pg.font.SysFont("Courier New", 18)
label = myfont.render("TestTestTest",0,(255,255,0))
surface.blit(label,(100,100))
pg.display.update()

# time.sleep( 3 )
waiting( surface )
