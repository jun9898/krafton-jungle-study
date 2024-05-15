import sys
input = sys.stdin.readline


def gcd(n, m):
    while n != 0:
        t = m%n
        (m,n) = (n,t)
    return abs(m)


def lcm(a, b):
    return a * b // gcd(a, b)


k = int(input())
for i in range(k):
    n, m = map(int, input().split())
    print(lcm(n, m))
