import sys
import math

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True


result = []

for i in arr:
    left, right = i//2, i//2
    while left > 0:
        if is_prime(left) and is_prime(right):
            result.append((left, right))
            break
        else:
            left -= 1
            right += 1

for i in result:
    print(*i)


