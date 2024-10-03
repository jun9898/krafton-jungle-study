import sys
from collections import deque

dy = [-1, 1, 0, 0, -1, 1, 1, -1]
dx = [0, 0, -1, 1, -1, -1, 1, 1]

input = sys.stdin.readline

def bfs(y, x):
    queue = deque([(y, x)])
    visited.add((y, x))
    while queue:
        cur_y, cur_x = queue.popleft()
        for i in range(8):
            ny, nx = cur_y + dy[i], cur_x + dx[i]
            if 0 <= ny < m and 0 <= nx < n and (ny, nx) not in visited and graph[ny][nx] == 1:
                visited.add((ny, nx))
                queue.append((ny, nx))


while True:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break
    graph = [list(map(int, input().split())) for _ in range(m)]
    visited = set()
    result = 0
    for i in range(m):
        for j in range(n):
            if (i, j) not in visited and graph[i][j] == 1:
                bfs(i, j)
                result += 1
    print(result)
