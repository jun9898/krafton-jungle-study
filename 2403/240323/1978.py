import math
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
res = 0

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


for i in arr:
    if is_prime(i):
        res += 1

print(res)