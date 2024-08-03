import sys
from collections import deque

input = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def check(t, y, x):
    tmp_count = 0
    for j in range(4):
        tmp_y, tmp_x = y + dy[j], x + dx[j]
        if 0 <= tmp_y < N and 0 <= tmp_x < M and graph[tmp_y][tmp_x] == 0:
            tmp_count += 1
    new_height = graph[y][x] - tmp_count
    if new_height <= 0:
        ice_positions.remove((y, x))
        return 0
    return new_height

def bfs(y, x, visited):
    queue = deque([(y, x)])
    visited.add((y, x))
    while queue:
        cur_y, cur_x = queue.popleft()
        for i in range(4):
            new_y, new_x = cur_y + dy[i], cur_x + dx[i]
            if 0 <= new_y < N and 0 <= new_x < M and graph[new_y][new_x] > 0 and (new_y, new_x) not in visited:
                visited.add((new_y, new_x))
                queue.append((new_y, new_x))

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

ice_positions = set()
for i in range(N):
    for j in range(M):
        if graph[i][j] > 0:
            ice_positions.add((i, j))

time = 0
while ice_positions:
    time += 1
    new_graph = [row[:] for row in graph]
    for y, x in list(ice_positions):
        new_graph[y][x] = check(time, y, x)

    graph = new_graph

    if len(ice_positions) == 0:
        print(0)
        break

    count = 0
    visited = set()
    for y, x in ice_positions:
        if (y, x) not in visited:
            bfs(y, x, visited)
            count += 1

    if count >= 2:
        print(time)
        break

else:
    print(0)
