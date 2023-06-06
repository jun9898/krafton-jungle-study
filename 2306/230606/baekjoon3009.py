from collections import deque

arrayX = deque()
arrayY = deque()

for i in range(3):
    x, y = map(int, input().split())
    arrayX.append(x)
    arrayY.append(y)

while True:
    if arrayX.count(arrayX[0]) != 2:
        resultX = arrayX[0]
        break
    else:
        arrayX.rotate(-1)

while True:
    if arrayY.count(arrayY[0]) != 2:
        resultY = arrayY[0]
        break
    else:
        arrayY.rotate(-1)

print(resultX, end=" ")
print(resultY)


