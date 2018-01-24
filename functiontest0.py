'''
向右划，若右边为0，移过去
        若与右边相等，相加
        若与右边不等，则进行下一个与右边的判断
        完成全部移动后，在左边的空白处随机生成一个数
        再次等待输入判断

'''

import random



def firstMap():
    a = [0, 0, 0, 0]
    i = random.randint(0,3)
    a[i] = random.randrange(2,5,2)
    i = random.randint(0, 3)
    a[i] = random.randrange(2, 5, 2)
    return a



def byebyeZero(num):
    b = num
    if key == 'r':
        for i in range(4):
            if b[i] == 0:
                b.pop(i)
                b.insert(0,0)

    if key == 'l':
        for i in range(4):
            if b[3-i] == 0:
                b.pop(3-i)
                b.insert(3, 0)
    return b

def addNum(k):
    k = res_byezero
    if key == 'r':
        for i in range(3):
            if k[3-i] == k[3-(i+1)]:
                k[3-i] = k[3-i]*2
                k.pop(3-(i+1))
                k.insert(0,0)
    elif key == 'l':
        for i in range(3):
            if k[i] == k[i+1]:
                k[i] = k[i+1]*2
                k.pop(i+1)
                k.insert(3,0)


    return k

firstNum = firstMap()
print(firstNum)
while True:
    key = input('input:')
    res_byezero = byebyeZero(firstNum)
    result = addNum(res_byezero)
    print(result)



