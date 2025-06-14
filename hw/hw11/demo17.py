# виконання перетворень у просторі

import pygame as pg
import time
# import numpy as np
from math import cos,sin,pi

maxx = 600
maxx2 = maxx//2
maxy = 600
maxy2 = maxy//2

def initGraphics(title):
    pg.init()
    bits = 32
    surface = pg.display.set_mode((maxx,maxy),0,bits)
    surface.fill((0,0,0))
    grid(surface)
    pg.event.clear()
    pg.event.set_allowed([pg.KEYUP, pg.MOUSEBUTTONUP])
    pg.display.set_caption(title)
    pg.display.update()
    return surface

def waiting( surface ):
    while True:
        event = pg.event.wait()
        global cube
        # якщо відпущено "пробіл"
        if (event.type == pg.KEYUP) and (event.key == 32):
            return
        # якщо відпущено "escape"
        elif (event.type == pg.KEYUP) and (event.key == 27):
            pg.quit()
            exit(0)
        # відпущено 'x': поворот навколо осі OX
        elif (event.type == pg.KEYUP) and (event.scancode == 27) and (event.key == 120):
            cube = transforms(cube,Rx)
            surface.blit(surface2,(0,0))
            drawCube(surface,cube)
            pg.display.update()
        elif (event.type == pg.KEYUP) and (event.scancode == 6) and (event.key == 99):
            print('c')
        elif (event.type == pg.KEYUP):
            print(event.type)
            print(event.scancode) 
            print(event.key)
        # якщо відпущено кнопку мишки
        elif (event.type == pg.MOUSEBUTTONUP):
            # surface.blit(surfaceReserve,(0,0))
            pg.draw.line(surface,(0,0,255),(0,event.pos[1]),(maxx,event.pos[1]))
            pg.draw.line(surface,(0,0,255),(event.pos[0],0),(event.pos[0],maxy))
            pg.draw.circle(surface,(0,255,0),(event.pos[0],event.pos[1]),3)
            pg.display.update()

def multVM(V,M):
    V2 = []
    for i in range(len(M)):
        s = 0
        for j in range(len(M)):
            s += V[j]*M[j][i]
        V2.append(int(s))
    return tuple(V2)

def multMM(M1,M2):
    MM = []
    for i in range(len(M1)):
        row = multVM(M1[i],M2)
        MM.append(list(row))
    return MM

def transforms(poly,M):
    newpoly = []
    for p in poly:
        p2 = multVM((p[0],p[1],p[2],1),M)
        newpoly.append((p2[0],p2[1],p2[2]))
    return newpoly

def grid(surface):
    for i in range(100,maxx,100):
        pg.draw.line(surface,(50,50,50),(i,0),(i,maxy))
    for i in range(100,maxy,100):
        pg.draw.line(surface,(50,50,50),(0,i),(maxx,i))
    pg.draw.line(surface,(100,100,100),(0,maxy2),(maxx,maxy2))
    pg.draw.line(surface,(100,100,100),(maxx2,0),(maxx2,maxy))

# рисування кубу
def drawCube(surface,cube):
    cube2 = [(c[0]+maxx2,c[1]+maxy2) for c in cube]
    pg.draw.polygon(surface,(255,0,0),cube2[:4],1)
    pg.draw.polygon(surface,(0,255,0),cube2[4:],1)
    for i in range(4):
        pg.draw.line(surface,(255,255,0),cube2[i],cube2[i+4])
    pg.display.update()

def makeT(x,y,z):
    T = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[x,y,z,1]]
    return T

surface = initGraphics( "Affine transformations" )
pg.display.update()
surface2 = surface.copy()

cos_phi = cos(pi/180)
sin_phi = sin(pi/180)
# матриця повороту навколо осі OX у просторі
Rx = [[1,0,0,0],
      [0,cos_phi,sin_phi,0],
      [0,-sin_phi,cos_phi,0],
      [0,0,0,1]]
# матриця повороту навколо осі OY у просторі
Rz = [[cos_phi,sin_phi,0,0],
      [-sin_phi,cos_phi,0,0],
      [0,0,1,0],
      [0,0,0,1]]

# задання координат куба
poly3d1 = [(-200,-190,-100),(200,-195,-95),(210,180,-102),(-195,190,-98)]
poly3d2 = [(-190,-185,+100),(210,-198,+110),(205,192,+105),(-205,195,+90)]
cube = []
cube.extend(poly3d1)
cube.extend(poly3d2)

drawCube(surface,cube)

waiting( surface )
