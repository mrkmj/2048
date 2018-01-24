import random
import sys

import pygame
from pygame.locals import *

score = 0

class AddNum(object):
    #实现相同数字翻倍
    def addNum_Right(self,moveMap,score):
        k = moveMap
        for j in range(4):
            for i in range(4):
                if k[j][3-i] == k[j][3-(i+1)]:
                    k[j][3-i] = k[j][3-i]*2
                    score = score + k[j][3-i]
                    middle = k[j]
                    middle.pop(3-(i+1))
                    middle.insert(0,0)
                    k[j] = middle

        return [k,score]

    def addNum_Left(self,moveMap,score):
        k = moveMap
        for j in range(4):
            for i in range(3):
                if k[j][i] == k[j][i+1]:
                    k[j][i] = k[j][i+1]*2
                    score = score + k[j][i]
                    middle = k[j]
                    middle.pop(i+1)
                    middle.insert(3,0)
                    k[j] = middle


        return [k,score]

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
    gg = AddNum()
    resultget = gg.addNum_Right(b,score)
    b = resultget[0]
    b = ariseOne(b)
    return [b,resultget[1]]

def byebyeZero_Left(num):
    b = num
    for j in range(4):
        for i in range(4):
            if b[j][3 - i] == 0:
                middle = b[j]
                middle.pop(3 - i)
                middle.insert(3, 0)
                b[j] = middle

    gg = AddNum()
    resultget = gg.addNum_Left(b, score)
    b = resultget[0]
    b = ariseOne(b)
    return [b, resultget[1]]

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

#开启游戏
def startgame(firstallMap):
    key = input('input:')
    if key == 'a':
       moveMap = byebyeZero_Left(firstallMap)

    elif key == 'd':
        moveMap = byebyeZero_Right(firstallMap)

    elif key == 'w':
        moveMap = byebyeZero_Up(firstallMap)
        #moveMap = byebyeZero_Up(firstallMap)

    elif key == 's':
        moveMap = byebyeZero_Down(firstallMap)

    #moveMap = byebyeZero(firstallMap)
    #middleMap = addNum(moveMap)


    return moveMap



firstallMap =firstMap()
for i in firstallMap:
    print(i)

display = firstallMap
while True:
    '''
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    #pygame.display.update()
    '''

    display = startgame(display)
    #showMap(display)
    for i in display:
        print(i)

    print(scroe)