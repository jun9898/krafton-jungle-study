import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

queue = deque([i for i in range(1, n+1)])

result = list(map(int, input().split()))

count = 0

for i in result:
    while queue[0] != i:
        if queue.index(i) <= len(queue) // 2:
            queue.rotate(-1)
            count += 1
        else:
            queue.rotate(1)
            count += 1
    queue.popleft()

print(count)