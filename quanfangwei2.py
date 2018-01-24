import random

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


#游戏结果显示
firstallMap =firstMap()
for i in firstallMap:
    print(i)

display = firstallMap
while True:
    display = startgame(display)
    for i in display:
        print(i)























