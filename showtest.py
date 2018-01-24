import random
import sys

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

    screen.blit(sucai, (i * 100, j * 100 + 100))

def showMap(num):
    s_map = num

    for j in  range(4):
        for i in range(4):
            if s_map[j][i] != 0:
                sucaiShow(s_map,j,i)



#界面初始化
pygame.init()
screen = pygame.display.set_mode((400,500))
pygame.display.set_caption('2048 --test0')
#background_color = 255,255,255
white = 255, 255, 255
screen.fill(white)
line_color = 0,0,0
line_with = 8

#画格子
for i in range(1,4):
    pygame.draw.line(screen, line_color,(i*100,100),(i*100,500))

for i in range(1,5):
    pygame.draw.line(screen, line_color,(0,i*100),(400,i*100))


#游戏结果显示
firstallMap =firstMap()
for i in firstallMap:
    print(i)

display = firstallMap
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    pygame.display.update()

    #display = startgame(display)

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_w] or pressed_keys[K_UP]:
        showMap(display)


