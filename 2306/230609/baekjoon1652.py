import sys
from collections import deque
import copy
input = sys.stdin.readline

n = int(input())

arr = list(deque(input().rstrip())for _ in range(n))
arrcopyx = copy.deepcopy(arr)

resultX = 0
resultY = 0
for i in arrcopyx:
    count = 0
    while i:
        if i[0] == ".":
            i.popleft()
            count += 1
        else:
            i.popleft()
            if count > 1:
                resultX += 1
                count = 0
            else:
                count = 0
        if len(i) == 0 and count > 1:
            resultX += 1
            count = 0
for _ in range(n):
    count = 0
    for j in range(n):
        if len(arr) == 0:
            break
        if arr[j][0] == ".":
            arr[j].popleft()
            count += 1
        else:
            arr[j].popleft()
            if count > 1:
                resultY += 1
                count = 0
            else:
                count = 0
    if count > 1:
        resultY += 1
        count = 0

print(resultX,resultY)
        




