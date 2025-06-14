# modified by Iryna Valeriivna Hrytsenko

# виконання паралельного перенесення та 
# розтягу/стиску

import pygame as pg
import time
# import numpy as np

maxx = 600
maxx2 = maxx//2
maxy = 600
maxy2 = maxy//2

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

# основний цикл програми: зчитування та обробка подій
def waiting( surface ):
    # організовуємо нескінченний цикл
    while True:
        event = pg.event.wait()
        global poly, dx, Dd, Ds
        # якщо відпущено "пробіл"
        if (event.type == pg.KEYUP) and (event.key == 32):
            return
        # якщо відпущено "escape"
        elif (event.type == pg.KEYUP) and (event.key == 27):
            # вихід з програми
            pg.quit()
            exit(0)
        # якщо відпущено стрілку "вправо"
        elif (event.type == pg.KEYUP) and (event.scancode == 79) and (event.key == 1073741903):
            # переміщуємо фігуру вправо
            # 1 виконуємо перетворення координат вершин ламаної
            poly = transforms(poly,Txr)
            # 2 рисуємо початкову поверхню вікна (з сіткою)
            surface.blit(surface2,(0,0))
            # 3 рисуємо оновлений полігон
            pg.draw.polygon(surface,(255,255,255),poly,1)
            # 4 виводимо результат у вікно
            pg.display.update()
        # якщо відпущено стрілку "вліво"
        elif (event.type == pg.KEYUP) and (event.scancode == 80) and (event.key == 1073741904):
            # переміщуємо фігуру вліво
            poly = transforms(poly,Txl)
            surface.blit(surface2,(0,0))
            pg.draw.polygon(surface,(255,255,255),poly,1)
            pg.display.update()
        # якщо відпущено стрілку "вгору"
        elif (event.type == pg.KEYUP) and (event.scancode == 82) and (event.key == 1073741906):
            # ERROR!!!
            # переміщуємо фігуру вгору
            poly = transforms(poly,Tyd)
            surface.blit(surface2,(0,0))
            pg.draw.polygon(surface,(255,255,255),poly,1)
            pg.display.update()
        # якщо відпущено стрілку "вниз"
        elif (event.type == pg.KEYUP) and (event.scancode == 81) and (event.key == 1073741905):
            # ERROR!!!
            # переміщуємо фігуру вниз
            poly = transforms(poly,Tyu)
            surface.blit(surface2,(0,0))
            pg.draw.polygon(surface,(255,255,255),poly,1)
            pg.display.update()
        # якщо відпущено на numpad клавішу "+"
        elif (event.type == pg.KEYUP) and (event.scancode == 87) and (event.key == 1073741911):
            # збільшуємо фігуру від центра
            poly = transforms(poly,T0)
            poly = transforms(poly,Dd)
            poly = transforms(poly,T1)
            surface.blit(surface2,(0,0))
            pg.draw.polygon(surface,(255,255,255),poly,1)
            pg.display.update()
        # якщо відпущено на numpad клавішу "-"
        elif (event.type == pg.KEYUP) and (event.scancode == 86) and (event.key == 1073741910):
            # зменшуємо фігуру до центра
            poly = transforms(poly,T0)
            poly = transforms(poly,Ds)
            poly = transforms(poly,T1)
            surface.blit(surface2,(0,0))
            pg.draw.polygon(surface,(255,255,255),poly,1)
            pg.display.update()

        # якщо відпущено на numpad клавішу "m"
        elif (event.type == pg.KEYUP) and (event.scancode == 16) and (event.key == 109):
            # збільшуємо коефіцієнт розтягу/стиснення
            # print("start",dx)
            dx += 0.05
            print("end",dx)
            Dd = [[1+dx,0,0],[0,1+dx,0],[0,0,1]]
            Ds = [[1-dx,0,0],[0,1-dx,0],[0,0,1]]
        # якщо відпущено на numpad клавішу "n"
        elif (event.type == pg.KEYUP) and (event.scancode == 17) and (event.key == 110):
            # зменшуємо коефіцієнт розтягу/стиснення
            # print("start",dx)
            dx -= 0.05
            print("end",dx)
            Dd = [[1+dx,0,0],[0,1+dx,0],[0,0,1]]
            Ds = [[1-dx,0,0],[0,1-dx,0],[0,0,1]]

        # якщо була відпущена будь-яка інша кнопка
        elif (event.type == pg.KEYUP):
            # виводимо коди кнопки на екран
            print(event.type)
            print(event.scancode)
            print(event.key)
        # якщо відпущено кнопку мишки
        elif (event.type == pg.MOUSEBUTTONUP):
            # surface.fill((0,0,0))
            # grid( surface )
            # очищаємо вікно та рисуємо дві лінії,
            # у точці перетину яких знаходиться курсор
            # мишки
            surface.blit(surface2,(0,0))
            pg.draw.line(surface,(0,0,255),(0,event.pos[1]),(maxx,event.pos[1]))
            pg.draw.line(surface,(0,0,255),(event.pos[0],0),(event.pos[0],maxy))
            pg.draw.circle(surface,(0,255,0),(event.pos[0],event.pos[1]),3)
            pg.display.update()

# функція множення вектора V на матрицю M
def multVM(V,M):
    V2 = []
    for i in range(len(M)):
        s = 0
        for j in range(len(M)):
            s += V[j]*M[j][i]
        V2.append(int(s))
    return tuple(V2)

# функція множення двох матриць M1 та M2
def multMM(M1,M2):
    MM = []
    for i in range(len(M1)):
        row = multVM(M1[i],M2)
        MM.append(list(row))
    return MM

# функція виконання перетворення, заданого матрицею M
# вхід:
#    poly - список координат вершин замкнутої ламаної
#    M    - матриця перетворення, яке треба виконати
# вихід:
#    newpoly - список нових координат вершин
def transforms(poly,M):
    newpoly = []
    for p in poly:
        p2 = multVM((p[0],p[1],1),M)
        newpoly.append((p2[0],p2[1]))
    return newpoly

# рисування сітки у вікні
def grid(surface):
    for i in range(100,maxx,100):
        pg.draw.line(surface,(50,50,50),(i,0),(i,maxy))
    for i in range(100,maxy,100):
        pg.draw.line(surface,(50,50,50),(0,i),(maxx,i))
    pg.draw.line(surface,(100,100,100),(0,maxy2),(maxx,maxy2))
    pg.draw.line(surface,(100,100,100),(maxx2,0),(maxx2,maxy))

# відображуємо вікно
surface = initGraphics( "Affine transformations" )
pg.display.update()
# зберігаємо поверхню для швидкої очистки вікна
surface2 = surface.copy()

# задаємо матриці перетворень
T0 = [[1,0,0],[0,-1,0],[-maxx2,maxy2,0]]
T1 = [[1,0,0],[0,-1,0],[maxx2,maxy2,0]]
Txr = [[1,0,0],[0,1,0],[5,0,1]]
Txl = [[1,0,0],[0,1,0],[-5,0,1]]
Tyu = [[1,0,0],[0,1,0],[0,5,1]]
Tyd = [[1,0,0],[0,1,0],[0,-5,1]]
dx = 0.05
Dd = [[1+dx,0,0],[0,1+dx,0],[0,0,1]]
Ds = [[1-dx,0,0],[0,1-dx,0],[0,0,1]]

# задаємо фігуру (трикутник)
poly = [(100,90),(500,280),(140,470)]

# рисуємо фігуру у вікні
pg.draw.polygon(surface,(255,255,255),poly,1)
pg.display.update()

# переходимо до основного циклу програми
waiting( surface )

# ToDo:
# - модифікуйте програму, виправивши помилки у блоках коду
#   64-67 та 72-75. Підказка: зверніть увагу на орієнтацію системи
#   координат у вікні. Відповідні блоки можна міняти, розширяти,
#   зменшувати тощо;
# - додайте збільшення/зменшення коефіцієнтів розтягу/стиснення з
#   кроком 0.05 (елементи керування придумайте самі); при зміні
#   корефіцієнта відповідне повідомлення повинне виводитись у
#   командному рядку
