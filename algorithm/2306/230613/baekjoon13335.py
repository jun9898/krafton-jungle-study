from collections import deque
import sys

input = sys.stdin.readline

n, w, l = map(int,input().split())
truck = deque(map(int, input().split()))

bridge = [0] * w
time = 0

while bridge:
    time += 1
    bridge.pop(0)
    if truck:
        if sum(bridge) + truck[0] <= l:
            bridge.append(truck.popleft())
        else:
            bridge.append(0)

print(time)

    


