import sys
input = sys.stdin.readline

m, n = map(int, input().split())
a = [1] * (n+1)

for i in range(2, n+1):
    if a[i] == 1:
        tmp = i
        for j in range(i*2, n+1, tmp):
            a[j] = 0

for i in range(m, n+1):
    if i == 1:
        continue
    if a[i] == 1:
        print(i)




