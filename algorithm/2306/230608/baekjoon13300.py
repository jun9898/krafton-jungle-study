import sys
input = sys.stdin.readline

n, m = map(int,input().split())
listM = [0 for _ in range(6)]
listW = [0 for _ in range(6)]

for i in range(n):
    x, y = map(int,input().split())
    if x == 0:
        listM[y-1] += 1
    else:
        listW[y-1] += 1

count = 0
for i in listM:
    while i > 0:
        count +=1
        i -= m
for i in listW:
    while i > 0:
        count +=1
        i -= m
print(count)

