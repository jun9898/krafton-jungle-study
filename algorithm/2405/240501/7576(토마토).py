import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and (ny, nx) not in visited and tomato[ny][nx] != -1:
                queue.append((ny, nx))
                tomato[ny][nx] = tomato[y][x] + 1
                visited.add((ny, nx))


M, N = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
visited = set()

for y in range(N):
    for x in range(M):
        if tomato[y][x] == 1:
            visited.add((y, x))
            queue.append((y, x))

bfs()
count = 0

for y in range(N):
    for x in range(M):
        if tomato[y][x] == 0:
            print(-1)
            exit()
        count = max(count, tomato[y][x])

print(count-1)

