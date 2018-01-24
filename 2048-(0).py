import pygame
from pygame.locals import *
import sys
import random
import time

position_x = random.randrange(0,300,100)
position_y = random.randrange(100,400,100)
firstposition = position_x, position_y, 100, 100

class Nummap(object):
    def __init__(self):
        #super(Nummap, self).__init__()
        pass


    def MoveUp(self):
        position_y += 100
        return position_y

    def MoveDown(self):
        position_y -= 100
        return position_y

'''
    def First_position_get(self):
        num_position = position_x, position_y, 100,100
        print(num_position)
        return num_position
'''
def position_get():
    position = position_x, position_y, 100, 100
    return position

pygame.init()
screen = pygame.display.set_mode((400,500))
pygame.display.set_caption('2048 --test0')
background_color = 0,0,200
pygame.draw.rect(screen, background_color, firstposition, 0)

num = Nummap()
#pygame.draw.rect(screen,background_color,position,0)
pygame.display.update()
x = position_x
y = position_y
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    # 接收玩家操作
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_w] or pressed_keys[K_UP]:
        y -= 100
        time.sleep(2)
    elif pressed_keys[K_s] or pressed_keys[K_DOWN]:
        y += 100
        '''
    elif pressed_keys[K_a] or pressed_keys[K_LEFT]:
        map.moveLeft()
    elif pressed_keys[K_d] or pressed_keys[K_RIGHT]:
        map.moveRight()
        '''
    position = x, y, 100, 100

    pygame.draw.rect(screen, background_color, position, 0)
    pygame.display.update()

'''
num = Nummap()
num.First_position_get()
num.MoveUp()
print(num.MoveUp())
num.First_position_get()
'''