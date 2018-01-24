import pygame
from pygame.locals import *
import sys

white = 255,255,255
blue = 0, 0, 200

#界面初始化
pygame.init()
screen = pygame.display.set_mode((400,500))
pygame.display.set_caption('2048 --test0')
#background_color = 255,255,255

screen.fill(white)
line_color = 0,0,0
line_with = 8

#画格子
for i in range(1,4):
    pygame.draw.line(screen, line_color,(i*100,100),(i*100,500))

for i in range(1,5):
    pygame.draw.line(screen, line_color,(0,i*100),(400,i*100))

sucai = pygame.image.load("cangku/2.png")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()


    screen.blit(sucai, (200, 100))
    pygame.display.update()
