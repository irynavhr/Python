# coding: cp1251

# �������� ����� ��������
# ToDo:
# 1. ³����������� ����� � ���, ����, ������������
#    ������ ������ � ���������� ������ ���������� ������
# 2. ������ ��������� ���� ������� ������ �� +10 ��� ���������� �� "+"
#    � -10 ��� ���������� �� "-"
#    ���������: (255,255,255)
#               "-": (245,245,245)
# 3. ��������� ��������� ���� ������ ��� ���������� �� ������ "f".
# 4. ��������� ��������� ���������/��������� ������ ������ ��� ����������
#    �� �������� �����/���� ��������.

import pygame as pg
import time
import random as rnd
import ctypes

def GetTextDimensions(text, points, font):
    class SIZE(ctypes.Structure):
        _fields_ = [("cx", ctypes.c_long), ("cy", ctypes.c_long)]

    hdc = ctypes.windll.user32.GetDC(0)
    hfont = ctypes.windll.gdi32.CreateFontA(points, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, font)
    hfont_old = ctypes.windll.gdi32.SelectObject(hdc, hfont)

    size = SIZE(0, 0)
    ctypes.windll.gdi32.GetTextExtentPoint32A(hdc, text, len(text), ctypes.byref(size))

    ctypes.windll.gdi32.SelectObject(hdc, hfont_old)
    ctypes.windll.gdi32.DeleteObject(hfont)

    return (size.cx, size.cy)



def initGraphics():
    pg.init()
    global surface
    surface = pg.display.set_mode(size=(maxx,maxy),depth=32)

    pg.event.set_blocked(None)
    pg.event.clear()
    pg.event.set_allowed([pg.KEYUP,pg.MOUSEBUTTONUP])

    surface.fill((50,50,50))
    pg.display.set_caption(f'show text: {flagShowText}')
    pg.display.update()

def printFigureNumber(coords):
    if not flagShowText:
        return
    global text_color
    graphtext = text.render(str(figureNumber),0,text_color)
    global surface
    surface.blit(graphtext,coords)

def processingEvents():
    global figureNumber
    global flagShowText
    global my_font_type, text, my_font_size
    while True:
        event = pg.event.wait()
        print(event)
        # if CTRL + Q or ESC
        if (event.type == pg.KEYUP) and ((event.scancode == 41) and \
           (event.key == 27) or \
           (event.scancode == 20) and (event.key == 113)):
            print('Bye!!!')
            exit(0)
        # text_color -10
        elif (event.type == pg.KEYUP) and (event.scancode == 45) and (event.key == 45):
            global text_color
            if text_color[0]>9:
                text_color = (text_color[0]-10, text_color[1]-10, text_color[2]-10)
            print(text_color)
        # text_color +10
        elif (event.type == pg.KEYUP) and (event.scancode == 46) and (event.key == 61):
            if text_color[0]<246:
                text_color = (text_color[0]+10, text_color[1]+10, text_color[2]+10)
            print(text_color)
        # my_font_type change     f                                                
        elif (event.type == pg.KEYUP) and (event.scancode == 9) and (event.key == 102):
            my_font_type = pg.font.get_fonts()[rnd.randint(0, 82)]
            text = pg.font.SysFont(my_font_type, my_font_size)
            print(my_font_type)


        # my_font_type change     -> up                                               
        elif (event.type == pg.KEYUP) and (event.scancode == 82) and (event.key == 1073741906):
            print("+")
            my_font_size += 1
            text = pg.font.SysFont(my_font_type, my_font_size)
            print(my_font_size)
            pg.display.update()
        # my_font_type change   -> down                                               
        elif (event.type == pg.KEYUP) and (event.scancode ==81 ) and (event.key == 1073741905):
            print("-")
            my_font_size -= 1
            text = pg.font.SysFont(my_font_type, my_font_size)
            print(my_font_size)
            pg.display.update()


        # if 'r'
        elif (event.type == pg.KEYUP) and (event.scancode == 21) and \
           (event.key == 114):
            # print('red rectangle')
            r = pg.Rect(rnd.randint(0,maxx-1),rnd.randint(0,maxy-1),
                        rnd.randint(10,maxx),rnd.randint(10,maxy))
            r[2] = r[2] if r[0]+r[2] < maxx else maxx-r[0]-1
            r[3] = r[3] if r[1]+r[3] < maxy else maxy-r[1]-1
            pg.draw.rect(surface,(255,0,0),r,5)
            figureNumber += 1
            curr_num_text_size = GetTextDimensions(str(figureNumber), my_font_size, my_font_type)
            print(curr_num_text_size)
            printFigureNumber(((r[0]+r[2]//2)-(curr_num_text_size[0]/2), (r[1]+r[3]//2)-((curr_num_text_size[1]-6)//2)))
            
            pg.display.update()
        # if 'c'
        elif (event.type == pg.KEYUP) and (event.scancode == 6) and \
           (event.key == 99):
            # print('cyan circle')
            figureNumber += 1
            curr_num_text_size = GetTextDimensions(str(figureNumber), my_font_size, my_font_type)
            c = ((rnd.randint(0,maxx)), (rnd.randint(0,maxy)))
            pg.draw.circle(surface,(200,200,255),c,20,5)
            printFigureNumber((c[0]-(curr_num_text_size[0]//2), c[1]-((curr_num_text_size[1]-6)//2)))
            pg.display.update()
        # if 't'
        elif (event.type == pg.KEYUP) and (event.scancode == 23) and \
           (event.key == 116):
            flagShowText = not flagShowText
            # print(flagShowText)
            pg.display.set_caption(f'show text: {flagShowText}')
            pg.display.update()
        # if left mouse button
        elif (event.type == pg.MOUSEBUTTONUP) and (event.button == 1):
            pos = event.pos
            width = 100
            height = 50
            figureNumber += 1
            curr_num_text_size = GetTextDimensions(str(figureNumber), my_font_size, my_font_type)
            r = pg.Rect(pos[0]-width//2,pos[1]-height//2,width,height)
            pg.draw.ellipse(surface,
                (rnd.randint(0,255),rnd.randint(0,255),rnd.randint(0,255)),
                r,3)

            printFigureNumber((pos[0] - (curr_num_text_size[0]//2),pos[1] - ((curr_num_text_size[1]-6)//2)))
            pg.display.update()
        # if right mouse button
        elif (event.type == pg.MOUSEBUTTONUP) and (event.button == 3):
            pos = event.pos
            width = 100
            height = 50
            figureNumber += 1
            curr_num_text_size = GetTextDimensions(str(figureNumber), my_font_size, my_font_type)
            r = pg.Rect(pos[0]-width//2,pos[1]-height//2,width,height)
            pg.draw.ellipse(surface,
                (rnd.randint(0,255),rnd.randint(0,255),rnd.randint(0,255)),
                r)
            printFigureNumber((pos[0]- (curr_num_text_size[0]//2),pos[1] - ((curr_num_text_size[1]-6)//2)))
            pg.display.update()

        # my_font_type change     f                                                
        else:
            print(event.key)

rnd.seed()
flagShowText = False
figureNumber = 0
maxx,maxy = 500,500

# print(len(pg.font.get_fonts()))

pg.font.init()
global my_font_type, my_font_size
my_font_type = "Bookman Old Style"
my_font_size = 18
text = pg.font.SysFont(my_font_type, my_font_size)
# text.bold = True
global text_color
text_color = (255, 255, 255)
initGraphics()
processingEvents()
