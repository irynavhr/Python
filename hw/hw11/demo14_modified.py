# modified by Iryna Valeriivna Hrytsenko

# ідея: разом з трикутником утворювати уявний прямокутник, за межами даного трикутника
#  цей прямокутниу має рухатись разом з наявним трикутником

# виконання переміщення фігури за допомогою мишки

import pygame as pg
import time
import random as rnd
import math 

maxx = 500
maxy = 500
mouseButtonPressed = False

a = (rnd.randint(100,maxx-100), rnd.randint(100,maxx-100)) 
b = (rnd.randint(100,maxx-100), rnd.randint(100,maxx-100)) 
c = (rnd.randint(100,maxx-100), rnd.randint(100,maxx-100)) 
li = []
li.append(a)
li.append(b)
li.append(c)
print(li)
x = min(a[0], b[0], c[0])
y = min(a[1], b[1], c[1])
w = max(a[0], b[0], c[0])-x
h = max(a[1], b[1], c[1])-y
rcolor = (rnd.randint(50,200),rnd.randint(50,200),rnd.randint(50,200))
rect = pg.Rect(x,y,w,h)





# ініціалізація графіки
def initGraphics(title):
    pg.init()
    bits = 32
    surface = pg.display.set_mode((maxx,maxy),0,bits)
    surface.fill((0,0,0))
    grid(surface)
    pg.event.clear()
    pg.event.set_allowed([ pg.KEYUP, pg.MOUSEBUTTONUP, 
        pg.MOUSEBUTTONDOWN, pg.MOUSEMOTION])
    pg.display.set_caption(title)
    pg.display.update()
    return surface

# визначення, чи знаходиться точка з координатами (x,y)
# у прямокутнику, заданому у змінній rect
# повертається функцією True чи False
def sqr_pol(a, b, c):
    side_a = math.sqrt(float((b[0]-c[0])**2 + (b[1]-c[1])**2))
    side_b = math.sqrt(float((a[0]-c[0])**2 + (a[1]-c[1])**2))
    side_c = math.sqrt(float((a[0]-b[0])**2 + (a[1]-b[1])**2))
    print(side_a, side_b, side_c)
    p = float((side_a+side_b+side_c)/2)
    s = math.sqrt(float(p*abs(p-side_a)*abs(p-side_b)*abs(p-side_c)))
    return s
    
def inRectangle(x,y):
    global rect
    global a, b, c
    h =[]
    h.append(x)
    h.append(y)
    h = tuple(h)
    print(h)
    if x >= rect[0] and x <= rect[0]+rect[2] and \
                y >= rect[1] and y <= rect[1]+rect[3]:
        sa = sqr_pol(h, a, b)
        sb = sqr_pol(h, b, c)
        sc = sqr_pol(h, a, c)
        sh = sqr_pol(a, b, c)
        print("4 площі ", sa, sb, sc, sh, sep="\n")
        dif = sa + sb + sc - sh
        print("dif", dif)
        if dif < 10 and dif > -10:
            return True
        



# основний цикл програми
def waiting( surface ):
    global mouseButtonPressed
    global xMouseOld
    global yMouseOld
    global a, b, c
    while True:
        event = pg.event.wait()
        print(event)
        # if space
        if (event.type == pg.KEYUP) and (event.key == 32):
                # зберігаємо попередні координати квадрата
                save_cur_pos = []
                save_cur_pos.append(rect[0])
                save_cur_pos.append(rect[1])
                print(save_cur_pos)
                # переміщуємо квадрат в центр
                rect.left = maxx//2 - rect.width//2
                rect.top = maxy//2 - rect.height//2
                # визначаємо вектор переміщення
                mov_vect = [rect[0]-save_cur_pos[0], rect[1]-save_cur_pos[1]]
                print(mov_vect)
                # змінюємо координати трикутника на mov_vect
                a = (a[0]+mov_vect[0], a[1]+mov_vect[1])
                b = (b[0]+mov_vect[0], b[1]+mov_vect[1])
                c = (c[0]+mov_vect[0], c[1]+mov_vect[1])
                # малюємо
                surface.fill((0,0,0))
                surface.blit(surfaceReserve,(0,0))
                # pg.draw.rect(surface,(255, 255, 255),rect,width=0)
                pg.draw.polygon(surface,rcolor,(a, b, c))
                pg.display.update()
        # якщо відпущено "escape"
        if (event.type == pg.KEYUP) and (event.key == 27):
            # вихід з програми
            pg.quit()
            exit(0)
        # якщо відпущено кнопку мишки
        elif (event.type == pg.MOUSEBUTTONUP):
            mouseButtonPressed = False
        # якщо переміщено мишку
        elif (event.type == pg.MOUSEMOTION):
            # print(event)
            # якщо при переміщенні не була натиснутою
            # кнопка мишки
            if not mouseButtonPressed:
                # переходимо на обробку нової події
                continue
            # при переміщенні мишки кнопка була натиснута
            x,y = event.pos
            # якщо курсор мишки знаходився у прямокутнику
            if inRectangle(x,y):
                # визначаємо зміщення курсора мишки
                dx = x - xMouseOld
                dy = y - yMouseOld
                # зберігаємо старі значення позиції курсора
                xMouseOld,yMouseOld = x,y
                # зміщуємо прямокутник на зміщення курсора
                # мишки
                rect.left += dx
                rect.top += dy
                # змінюємо координати трикутника на dx
                a = (a[0]+dx, a[1]+dy)
                b = (b[0]+dx, b[1]+dy)
                c = (c[0]+dx, c[1]+dy)
                # перерисовуємо прямокутник та трикутник
                surface.fill((0,0,0))
                surface.blit(surfaceReserve,(0,0))
                # pg.draw.rect(surface,(255, 255, 255),rect,width=0)
                pg.draw.polygon(surface,rcolor,(a, b, c))
                pg.display.update()
        # якщо натиснуто кнопку мишки
        elif (event.type == pg.MOUSEBUTTONDOWN):
            mouseButtonPressed = True
            xMouseOld,yMouseOld = event.pos

# рисування сітки у вікні
def grid(surface):
    for i in range(100,maxx,100):
        pg.draw.line(surface,(50,50,50),(i,0),(i,maxy))
    for i in range(100,maxy,100):
        pg.draw.line(surface,(50,50,50),(0,i),(maxx,i))

# відображуємо вікно
surface = initGraphics( "Mouse motion" )
pg.display.update()
# зберігаємо поверхню для швидкої очистки вікна
surfaceReserve = surface.copy()
# рисуємо трикутник
# pg.draw.rect(surface,(255, 255, 255),rect,width=0)
pg.draw.polygon(surface,rcolor,(a, b, c))
pg.display.update()




# переходимо до основного циклу програми
waiting( surface )

# ToDo:
# модифікуйте програму, щоб переміщувався не прямокутник,
# а зафарбований трикутник, координати та колір якого
# визначаються випадковим чином при запуску програми
