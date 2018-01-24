'''
    if key == 'w':
        for j in range(4):
            for i in range(4):
                zhuanzhi = []
                zhuanzhi.append(a[j][i])
            key = 'd'
            zhuanzhi = byebyeZero(zhuanzhi)
            for eachitem in zhuanzhi:
                for i in range(4):
                    a[j][i] = eachitem
'''

import random

#生成初始图
def firstMap():
    a = [0, 2, 0, 2]
    b = [0, 0, 0, 0]
    c = [0, 0, 0, 0]
    d = [0, 0, 0, 0]
    allMap = [a,b,c,d]
    i = random.randint(0,3)
    allMap[i][i] = random.randrange(2,5,2)
    i = random.randint(0, 3)
    allMap[i][i] = random.randrange(2, 5, 2)
    return allMap

def rotation_Clockwis(num):
    b = num
    for j in range(4):
        for i in range(4):
            b[j][i] = num[3-i][j]

    return b


def rotation_Anticlockwis(num):
    pass


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

    return b

def byebyeZero_Up(num):
    b = num
    for i in range(4):
        for j in range(4):
            zhuanzhi = []
            zhuanzhi.append(b[j][i])
        print(zhuanzhi)
        zhuanzhi = byebyeZero_Left(zhuanzhi)
        for k in range(4):
            b[j][k] = zhuanzhi[k]

    return b


'''
def byebyeZero(num):
    b = num
    #向右移动
    if key == 'd':
        for j in range(4):
            for i in range(4):
                if b[j][i] == 0:
                    middle = b[j]
                    middle.pop(i)
                    middle.insert(0,0)
                    b[j] = middle

    #向左移动
    if key == 'a':
        for j in range(4):
            for i in range(4):
                if b[j][3-i] == 0:
                    middle = b[j]
                    middle.pop(3-i)
                    middle.insert(3, 0)
                    b[j] = middle

    return b
'''
#实现相同数字翻倍
def addNum(moveMap):
    k = moveMap
    if key == 'd':
        for j in range(3):
            for i in range(3):
                if k[j][3-i] == k[j][3-(i+1)]:
                    k[j][3-i] = k[j][3-i]*2
                    middle = k[j]
                    middle.pop(3-(i+1))
                    middle.insert(0,0)
                    k[j] = middle

    elif key == 'a':
        for j in range(3):
            for i in range(3):
                if k[j][i] == k[j][i+1]:
                    k[j][i] = k[j][i+1]*2
                    middle = k[j]
                    middle.pop(i+1)
                    middle.insert(3,0)
                    k[j] = middle

    #返回middleMap
    return k

firstallMap = firstMap()
for i in firstallMap:
    print(i)
while True:
    key = input('input:')
    if key == 'a':
       moveMap = byebyeZero_Left(firstallMap)

    elif key == 'd':
        moveMap = byebyeZero_Right(firstallMap)

    elif key == 'w':
        moveMap = rotation_Clockwis(firstallMap)
        #moveMap = byebyeZero_Up(firstallMap)


    #moveMap = byebyeZero(firstallMap)
    #middleMap = addNum(moveMap)
    for i in moveMap:
        print(i)























