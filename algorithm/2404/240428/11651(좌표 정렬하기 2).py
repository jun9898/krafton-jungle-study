import sys
input = sys.stdin.readline

n = int(input())
res = []
for i in range(n):
    res.append(list(map(int,input().split())))

res.sort(key=lambda x: (x[1], x[0]))

for i in res:
    print(*i)
