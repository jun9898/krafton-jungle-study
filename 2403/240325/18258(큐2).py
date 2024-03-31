import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

queue = deque()

for _ in range(n):
    commend = list(input().split())

    if commend[0] == 'push':
        queue.append(commend[1])
    elif commend[0] == 'pop':
        if len(queue) != 0: print(queue.popleft())
        else: print(-1)
    elif commend[0] == 'size':
        print(len(queue))
    elif commend[0] == 'empty':
        if len(queue) == 0: print(1)
        else: print(0)
    elif commend[0] == 'front':
        if len(queue) != 0: print(queue[0])
        else: print(-1)
    elif commend[0] == 'back':
        if len(queue) != 0: print(queue[-1])
        else: print(-1)
