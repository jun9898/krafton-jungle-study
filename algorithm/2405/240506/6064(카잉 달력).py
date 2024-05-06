import sys
input = sys.stdin.readline


def num(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1


n = int(input())

for i in range(n):
    M, N, x, y = map(int,input().split())
    print(num(M, N, x, y))