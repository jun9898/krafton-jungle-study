import sys
from collections import deque

input = sys.stdin.readline

arr = deque(i for i in range(1, int(input())+1))

while arr:
    print(arr.popleft(), end=" ")
    arr.rotate(-1)