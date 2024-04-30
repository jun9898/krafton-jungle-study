import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            print(dist[x])
            break
        # dp table 생각남
        for next in (x - 1, x + 1, x * 2):
            if 0 <= next <= MAX and not dist[next]:
                dist[next] = dist[x] + 1
                queue.append(next)


MAX = 10 ** 5
dist = [0] * (MAX + 1)
n, k = map(int, input().split())
bfs()

