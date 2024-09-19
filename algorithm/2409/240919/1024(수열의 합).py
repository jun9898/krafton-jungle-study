import sys
input = sys.stdin.readline

N, L = map(int, input().split())

for i in range(L, 101):
    tmp = N - (i * (i + 1) // 2)
    if tmp % i == 0:
        tmp2 = tmp // i
        if tmp2 + 1 >= 0:
            print(*(i for i in range(tmp2 + 1, tmp2 + i + 1)))
            break
else:
    print(-1)
