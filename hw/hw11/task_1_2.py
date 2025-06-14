# Hrytsenko Iryna Valeriivna
# expression "є"

import pygame as pg
from math import floor, pi, sin, cos
import time

def prepare_surf():
   disloc_k = 2
   # відображення системи координат
   dark_gray = (100,100,100)
   # рисуємо систему координат (уявну - X'OY')
   # рисуємо горизонтальну лінію системи координат
   pg.draw.line(surface,dark_gray,(0,y0),(h_x,y0),width=2)
   # рисуєсо стрілочку для осі координат
   pg.draw.line(surface,dark_gray,(h_x-16,y0+8),(h_x-1,y0),width=2)
   pg.draw.line(surface,dark_gray,(h_x-16,y0-8),(h_x-1,y0),width=2)
   # рисуємо вертикальну лінію системи координат
   pg.draw.line(surface,dark_gray,(x0,0),(x0,h_y),width=2)
   # рисуєсо стрілочку для осі координат
   pg.draw.line(surface,dark_gray,(x0,1),(x0-8,16),width=2)
   pg.draw.line(surface,dark_gray,(x0,1),(x0+8,16),width=2)
   pg.display.update()
   # рисуємо назви кординат 
   global text, numText
   graphtext = text.render("O",0,text_letter_color)
   surface.blit(graphtext,(x0 + disloc_k, y0 + disloc_k))
   graphtext = text.render("X",0,text_letter_color)
   surface.blit(graphtext,(h_x - disloc_k*16, y0 - disloc_k*16))
   graphtext = text.render("Y",0,text_letter_color)
   surface.blit(graphtext,(x0 - disloc_k*14, disloc_k*4))
   # рисуємо числа вздовж осей
   for i in list((i-9)*50 for i in range(0,20)): 
      if i == 0 :
         continue
      graphtext = numText.render(str(i*x_max/(h_x/2)),0,text_num_color)  
      surface.blit(graphtext,(x0 + disloc_k*3, y0 - i - 2)) 
      graphtext = numText.render(str(i*y_max/(h_y/2)),0,text_num_color)  
      surface.blit(graphtext,(x0 + i - 11, y0 + disloc_k*3))

def def_y(t):
   return a*(sin(t) - t*cos(t))

def def_x(t):
   return a*(cos(t) - t*sin(t))


def culc_func():
    # розрахунок точок графіка та збереження в список
    t1 = t_min 
    while t1 <= t_max:
        x1 = def_x(t1)
        y1 = def_y(t1)
        x = int(floor(x1*k_x + x0))
        y = int(floor(y0 - y1*k_y))
        if x >= 0 and x <= h_x and y >= 0 and y <= h_y:
            save_points.append((x, y))
        t1 += dx

def print_func():                   
    for i in save_points:
        pg.draw.circle(surface, pointcolor, (i[0],i[1]), 2)
    pg.display.update()

def processingEvents():
    while True:
        event = pg.event.wait()
        print(event)

        global x0, y0, k_x, k_y,dx, save_points, a

        # if CTRL + Q or ESC
        if (event.type == pg.KEYUP) and ((event.scancode == 41) and \
            (event.key == 27) or \
            (event.scancode == 20) and (event.key == 113)):
            print('Bye!!!')
            exit(0)
        # ліва кнопка миші
        elif (event.type == pg.MOUSEBUTTONUP) and (event.button == 1):
            pos = event.pos
            x0, y0 = pos[0], pos[1]
            k_x *= 1.5
            k_y *= 1.5
            surface.fill((255,255,255))
            prepare_surf()
            save_points = []
            culc_func()
            print_func()
        # права кнопка миші
        elif (event.type == pg.MOUSEBUTTONUP) and (event.button == 3):
            x0, y0 = 255, 255
            k_x, k_y, dx = store_ks[0], store_ks[1], store_ks[2]
            surface.fill((255,255,255))
            prepare_surf()
            save_points = []
            culc_func()
            print_func()
        # "+"
        elif (event.type == pg.KEYUP) and (event.scancode == 46) and (event.key == 61) :
            print("+")
            dx /= 2
            surface.fill((255,255,255))
            prepare_surf()
            save_points = []
            culc_func()
            print_func()
        # "-"
        elif (event.type == pg.KEYUP) and (event.scancode == 45) and (event.key == 45) :
            print("-")
            dx *= 2
            surface.fill((255,255,255))
            prepare_surf()
            save_points = []
            culc_func()
            print_func()
        # зміна параметра а стрілочками "вгору" та "вниз"
        elif (event.type == pg.KEYUP) and (event.scancode == 82) and (event.key == 1073741906) :
            print("Збільшення пелюсток")
            a += 1
            surface.fill((255,255,255))
            prepare_surf()
            save_points = []
            culc_func()
            print_func()
        elif (event.type == pg.KEYUP) and (event.scancode == 81) and (event.key == 1073741905) :
            print("Зменшення пелюсток")
            a -= 1             
            surface.fill((255,255,255))
            prepare_surf()
            save_points = []
            culc_func()
            print_func()
    
        elif (event.type == pg.KEYUP) and (event.scancode == 58) and (event.key == 1073741882) :
            print("""Довідка: 
    Натисніть ESC, щоб вийти з програми  
    Натисніть +, щоб збільшити крок параметра t
    Натисніть -, щоб зменшити крок параметра t
    Регулюйте параметр a стрілками вгору та вниз
    Натисніть ліву кнопку миші щоб приблизити
    Натисніть праву кнопку миші щоб повернути маштаб до початкового""")
            



         
# розміри вікна
h_x, h_y = 500, 500
# координати початку системи координат графіка
global x0, y0
# x0, y0 = 250, 350
x0, y0 = 250, 250
# діапазон зміни параметра
t_min, t_max = -4.5, 4.5
# t_min, t_max = 0, 15
a = 20
# діапазон абсцис графіка
x_min, x_max = -250, 250
# x_min, x_max = -2*pi,2*pi
# діапазон ординат графіка
y_min, y_max = -250, 250
# y_min, y_max = -0.25, 0.25
# крок зміни параметра
dx = 0.01
# розрахунок коефіцієнтів масштабування 
h1_x = x_max - x_min
h1_y = y_max - y_min
k_x = h_x / h1_x
k_y = h_y / h1_y
store_ks = (k_x, k_y, dx)
# колір точки
pointcolor = (0,0,255)

# ініціалізація графіки 
pg.init()
surface = pg.display.set_mode(
   size=(h_x,h_y),depth=32)
surface.fill((255,255,255))
pg.display.set_caption("Graphs-2")
pg.display.update()

# text 
text = pg.font.SysFont("bahnschrift", 26)
numText = pg.font.SysFont("arial", 14)
text.bold = False
text.italic = True
numText.bold = False
numText.italic = True
text_letter_color = (0, 0, 0)
text_num_color = (120, 120, 200)

# відображення графіку на екран
prepare_surf()
save_points = []
culc_func()
print_func()
pg.display.update()

# обробка подій миші та клавіатури
processingEvents()
# time.sleep( 5 )
