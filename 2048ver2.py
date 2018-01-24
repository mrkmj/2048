import random
import sys
import time

import pygame
from pygame.locals import *


#生成初始图
def firstMap():
    a = [0, 0, 0, 0]
    b = [0, 0, 0, 0]
    c = [0, 0, 0, 0]
    d = [0, 0, 0, 0]
    allMap = [a,b,c,d]
    i = random.randint(0,3)
    allMap[i][i] = random.randrange(2,5,2)
    i = random.randint(0, 3)
    allMap[i][i] = random.randrange(2, 5, 2)
    return allMap

#数字匹配显示
def sucaiShow(num,j,i):
    s_map = num
    if s_map[j][i] == 2:
        sucai = pygame.image.load("cangku/2.png")

    if s_map[j][i] == 4:
        sucai = pygame.image.load("cangku/4.png")

    if s_map[j][i] == 8:
        sucai = pygame.image.load("cangku/8.png")

    if s_map[j][i] == 16:
        sucai = pygame.image.load("cangku/16.png")

    if s_map[j][i] not in [2,4,8,16]:
        sucai = pygame.image.load("cangku/rest.png")

    screen.blit(sucai, (i * 100, j * 100 + 100))

#数字图片显示在图上
def showMap(num):
    s_map = num
    startupScreen()
    for j in  range(4):
        for i in range(4):
            if s_map[j][i] != 0:
                sucaiShow(s_map,j,i)

#随机弹出一个2或4
def ariseOne(num):
    if (0 in num[0]) or (0 in num[1]) or (0 in num[2]) or (0 in num[3]):
        while True:
            j = random.randint(0,3)
            i = random.randint(0,3)
            if num[j][i] == 0:
                num[j][i] = random.randrange(2, 5, 2)
                break
            else:
                continue
    else:
        print('lose')

    return num

#矩阵旋转
def rotation_Clockwise(num):
    b = []

    for j in range(4):
        t = []
        for i in range(4):
            t.append(num[3-i][j])
        b.append(t)

    return b

def rotation_Anticlockwise(num):
    b = []

    for i in range(4):
        t = []
        for j in range(4):
            t.append(num[j][3-i])
        b.append(t)

    return b

#把数组中的零先提取，在把数字移到一边
def byebyeZero_Right(num):
    b = num
    for j in range(4):
        for i in range(4):
            if b[j][i] == 0:
                middle = b[j]
                middle.pop(i)
                middle.insert(0, 0)
                b[j] = middle

    b = addNum_Right(b)
    b = ariseOne(b)
    return b

def byebyeZero_Left(num):
    b = num
    for j in range(4):
        for i in range(4):
            if b[j][3 - i] == 0:
                middle = b[j]
                middle.pop(3 - i)
                middle.insert(3, 0)
                b[j] = middle

    b = addNum_Left(b)
    b = ariseOne(b)
    return b

def byebyeZero_Up(num):
    b = num
    zhuanzhi = rotation_Clockwise(b)
    zhuanzhi = byebyeZero_Right(zhuanzhi)

    zhuanzhi = rotation_Anticlockwise(zhuanzhi)

    return zhuanzhi

def byebyeZero_Down(num):
    b = num
    zhuanzhi = rotation_Clockwise(num)
    zhuanzhi = byebyeZero_Left(zhuanzhi)

    zhuanzhi = rotation_Anticlockwise(zhuanzhi)

    return zhuanzhi

#实现相同数字翻倍
def addNum_Right(moveMap):
    k = moveMap
    for j in range(4):
        for i in range(4):
            if k[j][3-i] == k[j][3-(i+1)]:
                k[j][3-i] = k[j][3-i]*2
                middle = k[j]
                middle.pop(3-(i+1))
                middle.insert(0,0)
                k[j] = middle

    return k

def addNum_Left(moveMap):
    k = moveMap
    for j in range(4):
        for i in range(3):
            if k[j][i] == k[j][i+1]:
                k[j][i] = k[j][i+1]*2
                middle = k[j]
                middle.pop(i+1)
                middle.insert(3,0)
                k[j] = middle

    return k

#开启游戏
def startgame(firstallMap):
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_w] or pressed_keys[K_UP]:
       moveMap = byebyeZero_Up(firstallMap)

    elif pressed_keys[K_s] or pressed_keys[K_DOWN]:
        moveMap = byebyeZero_Down(firstallMap)

    elif pressed_keys[K_a] or pressed_keys[K_LEFT]:
        moveMap = byebyeZero_Left(firstallMap)


    elif pressed_keys[K_d] or pressed_keys[K_RIGHT]:
        moveMap = byebyeZero_Right(firstallMap)

    print(moveMap)
    #return moveMap

#界面初始化
def startupScreen():


    pygame.display.set_caption('2048 --test0')
    background_color = 0,0,200
    white = 238, 228, 218
    screen.fill(white)
    line_color = 0,0,0
    line_with = 8

    #画格子
    for i in range(1,4):
        pygame.draw.line(screen, line_color,(i*100,100),(i*100,500))

    for i in range(1,5):
        pygame.draw.line(screen, line_color,(0,i*100),(400,i*100))

pygame.init()
screen = pygame.display.set_mode((400,500))
startupScreen()

#游戏结果显示
firstallMap =firstMap()
for i in firstallMap:
    print(i)

display = firstallMap
clock = pygame.time.Clock()
showMap(display)
while True:
    #time.sleep(0.1)
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    pygame.display.update()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_w] or pressed_keys[K_UP]:
        display = byebyeZero_Up(display)

    elif pressed_keys[K_s] or pressed_keys[K_DOWN]:
        display = byebyeZero_Down(display)

    elif pressed_keys[K_a] or pressed_keys[K_LEFT]:
        display = byebyeZero_Left(display)


    elif pressed_keys[K_d] or pressed_keys[K_RIGHT]:
        display = byebyeZero_Right(display)

    elif pressed_keys[K_q]:
        display = olddisplay

    olddisplay = display




    #display = startgame(display)
    showMap(display)
    #for i in display:
        #print(i)

























