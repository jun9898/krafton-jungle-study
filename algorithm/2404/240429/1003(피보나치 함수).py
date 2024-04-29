import sys
input = sys.stdin.readline


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if memo[n] != 0:
        return memo[n]
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]


n = int(input())
for i in range(n):
    zero = 0
    one = 1
    memo = [0] * 41
    a = int(input())
    fibonacci(a)
    if a == 0:
        print(1, 0)
    elif a == 1:
        print(0, 1)
    elif a == 2:
        print(1, 1)
    else:
        print(memo[a-1], memo[a])
