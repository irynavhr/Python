# coding: cp1251

import pygame as pg
from math import floor, sin, cos
import time

def f(x):
  return sin(x)*cos(x)/3

windowWidth  = 500
windowHeight = 500

pg.init()
surface = pg.display.set_mode(
   size=(windowWidth,windowHeight),depth=32)
surface.fill((255,255,255))
pg.display.set_caption("Graphs-1")
pg.display.update()

dark_gray = (100,100,100)

# рисуємо систему координат (уявну - X'OY')
# рисуємо горизонтальну лінію системи координат
pg.draw.line(surface,dark_gray,
              (0,windowHeight//2),
              (windowWidth,windowHeight//2),
              width=2)
# рисуємо вертикальну лінію системи координат
pg.draw.line(surface,dark_gray,
              (windowWidth//2,0),
              (windowWidth//2,windowHeight),
              width=2)
pg.display.update()

# визначимо координати початку уявної системи координат
# у реальній (віконній) системі координат
Ox = windowWidth // 2
Oy = windowWidth // 2

# виберемо колір точок
pointcolor = (255,0,0)

# min_x
# max_x
# min_y
# max_y

# знайдемо потрібні значення
min_x = -101/50
max_x = min_x
min_y = f(min_x)
max_y = min_y
for x in range(-101,101,1):
   xd = x/50
   if xd < min_x:
      min_x = xd
   if xd > max_x:
      max_x = xd
   yd = f(xd)
   if yd < min_y:
      min_y = yd
   if yd > max_y:
      max_y = yd

# візьмемо абсциси від - -100 до 100
for x in range(-101,101,1):
   xd = x/50
   yd = f(xd)
   x = floor((xd-min_x)/(max_x-min_x)*windowWidth)
   y = floor((yd-min_y)/(max_y-min_y)*windowHeight)
   # отримуємо координати точки у реальній системі координат
   pointcoords = (x,windowHeight-y)
   pg.draw.circle(surface, pointcolor, pointcoords, 2)
   pg.display.update()

time.sleep( 5 )
