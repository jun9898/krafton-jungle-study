import sys
input = sys.stdin.readline

n, m = map(int, input().split())


def gcd(n, m):
    while n != 0:
        t = m%n
        (m,n) = (n,t)
    return abs(m)

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(n, m))
print(lcm(n, m))
