
import sys
from collections import deque
input = sys.stdin.readline

y, x, n = map(int, input().split())
array = []
arrayAppend = deque()

for i in range(y):
    array.append(list(map(str, input().split())))

result = [[0]*x for i in range(y)]
print(result)

loop = min(x,y) // 2
for i in range(loop):
    arrayAppend.clear()
    arrayAppend.extend(array[i][i:x-i])
    arrayAppend.extend([row[x-1-i] for row in array[i+1:y-i-1]])
    arrayAppend.extend(array[y-1-i][i:x-i][::-1])
    arrayAppend.extend([row[i][::-1] for row in array[i+1:y-i-1]])
    print(arrayAppend)

    arrayAppend.rotate(-n)

    for j in range(i,x-i):
        result[i][j] = arrayAppend.popleft()
    for j in range(i+1,y-1-i):
        result[j][x-1-i] = arrayAppend.popleft()
    for j in range(x-i-1,i-1,-1):
        result[y-1-i][j] = arrayAppend.popleft()
    for j in range(y-i-2,i,-1):
        result[j][i] = arrayAppend.popleft()

for i in result:
    print(" ".join(i))


    

