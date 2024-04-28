import sys
from collections import deque
input = sys.stdin.readline


def round_up(n):
    integer = int(n)
    decimal = n - integer

    if decimal*10 >= 5:
        return integer + 1
    else:
        return integer


n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

if len(arr) == 0:
    print(0)
    sys.exit()

arr.sort()
arr = deque(arr)

n = round_up(n * 0.15)

for i in range(n):
    arr.popleft()
    arr.pop()

length = len(arr)
ans = sum(arr)

print(round_up(ans / length))


