import sys
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

input = sys.stdin.readline

def bfs(y, x, visited):
    queue = deque([(y, x, 0)])
    tmp = 0
    while queue:
        curY, curX, time = queue.popleft()
        for i in range(4):
            newY, newX = curY + dy[i], curX + dx[i]
            if 0 <= newY < n and 0 <= newX < m and graph[newY][newX] == "L" and (newY, newX) not in visited:
                queue.append((newY, newX, time + 1))
                visited.add((newY, newX))
                continue
        tmp = max(tmp, time)
    return tmp

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

result = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == "L":
            visited = {(i, j)}
            result = max(result, bfs(i, j, visited))

print(result)

