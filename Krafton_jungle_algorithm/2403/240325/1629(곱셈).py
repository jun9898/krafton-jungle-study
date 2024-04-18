import sys
input = sys.stdin.readline

def solve(a,b,c):
    if b == 1:
        return a % c
    temp = solve(a, b//2, c)
    if b % 2 == 0:
        return (temp * temp) % c
    elif b % 2 == 1:
        return ((temp * temp) % c) * a % c


a, b, c = map(int,input().split())
print(solve(a,b,c))