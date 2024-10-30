import sys
from collections import deque

input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def planting():
    global queue
    for i in range(R):
        for j in range(C):
            if graph[i][j] == "O":
                queue.append((i, j))

def explosion():
    global queue, graph
    while queue:
        cur_y, cur_x = queue.popleft()
        graph[cur_y][cur_x] = "."
        for i in range(4):
            new_y, new_x = (cur_y + dy[i], cur_x + dx[i])
            if 0 <= new_y < R and 0 <= new_x < C and graph[new_y][new_x] == "O":
                graph[new_y][new_x] = "."

R, C, N = map(int, input().split())
queue = deque()

graph = [list(input().rstrip()) for _ in range(R)]

for i in range(1, N + 1):
    if i == 1:
        planting()
    elif i % 2 == 1:
        explosion()
        planting()
    else:
        graph = [['O' for _ in range(C)] for _ in range(R)]

for i in graph:
    print("".join(i))



