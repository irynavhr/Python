# modified by Iryna Valeriivna Hrytsenko

# виконання повороту навколо початку координат

from math import sqrt, pi, sin, cos
import pygame as pg
import time
from sys import exit

maxx = 500
maxy = 500
xO = 250
yO = 250

# ініціалізація графіки
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

# рисування сітки у вікні
def grid(surface):
   for i in range(50,maxx,50):
      pg.draw.line(surface,(50,50,50),(i,0),(i,maxy))
   for i in range(50,maxy,50):
      pg.draw.line(surface,(50,50,50),(0,i),(maxx,i))

# створення матриці повороту
def makeR( alpha ):
   R = [ [ cos(alpha),  sin(alpha), 0 ],
         [ -sin(alpha), cos(alpha), 0 ],
         [ 0,           0,          1 ] ]
   return R

# множення вектора на матрицю
def multVM( p,m ):
   r = [ 0,0,0 ]
   r[0] = p[0]*m[0][0] + p[1]*m[1][0] + p[2]*m[2][0]
   r[1] = p[0]*m[0][1] + p[1]*m[1][1] + p[2]*m[2][1]
   r[2] = p[0]*m[0][2] + p[1]*m[1][2] + p[2]*m[2][2]
   return r

# відображення початкового вікна
surface = initGraphics("Demo rotation")

# створення матриці повороту на 5 градусів
R = makeR( 0.01*pi/180 )
# вибираємо початкові координати трикутника:
pol = [( -115,70,0 ), ( 0,-130,0 ), ( 115,70,0 )]
pg.draw.polygon(surface,(255,255,0),((xO+pol[0][0], yO+pol[0][1]), (xO+pol[1][0], yO+pol[1][1]), (xO+pol[2][0], yO+pol[2][1])),1)
pg.display.update()
time.sleep( 1 )

# повертаємо точку постійно на 5 градусів навколо
# початку координат за годинниковою стрілкою

for i in range(0,10000):
      # замальовуємо попереднє положення точки чорним кольором
      # surface.set_at( ( xO+int(round(point[0])),yO+int(round(point[1])) ),(0,0,0) )
      pg.draw.polygon(surface,(0,0,0),((xO+pol[0][0], yO+pol[0][1]), (xO+pol[1][0], yO+pol[1][1]), (xO+pol[2][0], yO+pol[2][1])),1)
      # розраховуємо координати наступного положення точки
      for i in range(3):
         pol[i] = multVM( pol[i],R )
      # виводимо точку у вікно
      # surface.set_at( ( xO+int(round(point[0])),yO+int(round(point[1])) ),(255,255,0) )
      grid(surface)
      pg.draw.polygon(surface,(255,255,0),((xO+pol[0][0], yO+pol[0][1]), (xO+pol[1][0], yO+pol[1][1]), (xO+pol[2][0], yO+pol[2][1])),1)
      # оновлюємо вікно
      pg.display.update()
      # пауза - 1 сек
      time.sleep( 0.001 )

# ToDo:
# модифікуйте програму, реалізувавши наступне:
# 1) у програмі початок системи координат вважається у верхньому
#    лівому куті вікна. Перенесіть початок системи координат у центр
#    вікна;
# 2) розробіть демонстрацію повороту довільного трикутника, усередині
#    якого знаходиться центр координат, на 1 градус за годинниковою
#    стрілкою навколо центру координат
