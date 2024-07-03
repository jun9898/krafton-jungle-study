import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def check(t, y, x):
    tmp_count = 0
    for j in range(4):
        tmp_y, tmp_x = y + dy[j], x + dx[j]
        if 0 <= tmp_y < N and 0 <= tmp_x < M and graph_3d[t][tmp_y][tmp_x] == 0:
            tmp_count += 1

    graph_3d[t+1][y][x] = graph_3d[t][y][x] - tmp_count
    if graph_3d[t+1][y][x] < 0:
        graph_3d[t+1][y][x] = 0


def bfs(t, y, x, visited):
    queue = deque([(y, x)])
    visited.add((y, x))
    while queue:
        cur_y, cur_x = queue.popleft()
        for i in range(4):
            new_y, new_x = cur_y + dy[i], cur_x + dx[i]
            if 0 <= new_y < N and 0 <= new_x < M and graph_3d[t][new_y][new_x] > 0 and (new_y, new_x) not in visited:
                visited.add((new_y, new_x))
                queue.append((new_y, new_x))


N, M = map(int, input().split())
graph = []

max_ice = 0
for i in range(N):
    tmp = list(map(int, input().split()))
    max_ice = max(max_ice, max(tmp))
    graph.append(tmp)


graph_3d = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(max_ice + 1)]

for i in range(N):
    for j in range(len(graph[i])):
        graph_3d[0][i][j] = graph[i][j]

for t in range(max_ice-1):
    for i in range(N):
        for j in range(M):
            if graph_3d[t][i][j] > 0:
                check(t, i, j)
    print(*graph_3d[t], sep='\n')
    print()

    count = 0
    visited = set()
    for i in range(N):
        for j in range(M):
            if graph_3d[t+1][i][j] > 0 and (i, j) not in visited:
                bfs(t+1, i, j, visited)
                count += 1
    if count >= 2:
        print(t+1)
        exit(0)
print(0)

