a = [1, 2, 0, 2]
b = [0, 0, 0, 0]
c = [1, 0, 0, 0]
d = [0, 3, 0, 0]
allMap = [a,b,c,d]

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
moveMap = rotation_Clockwise(allMap)
print('-'*30)
for i in moveMap:
    print(i)