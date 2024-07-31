import sys
input = sys.stdin.readline

listx = []
listy = []

n = int(input())

for i in range(n):
    x,y = map(int,input().split())
    listx.append(x)
    listy.append(y)

if n <= 1:
    print(0)
    sys.exit
else:
    print((max(listx)-min(listx)) * (max(listy)-min(listy)))
