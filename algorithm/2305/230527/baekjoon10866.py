import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
result = deque()

for i in range(n):
    commend = list(map(str, input().split()))
    if "push_front" in commend:
        result.appendleft(commend[-1])
    if "push_back" in commend:
        result.append(commend[-1])
    if "pop_front" in commend:
        if len(result) != 0:
            print(result.popleft())
        else:
            print(-1)
    if "pop_back" in commend:
        if len(result) != 0:
            print(result.pop())
        else:
            print(-1)
    if "size" in commend:
        print(len(result))
    if "empty" in commend:
        if len(result) <= 0:
            print(1)
        else:
            print(0)
    if "front" in commend:
        if len(result) <= 0:
            print(-1)
        else:
            print(result[0])
    if "back" in commend:
        if len(result) <= 0:
            print(-1)
        else:
            print(result[-1])

# 기본적인 deque문제

