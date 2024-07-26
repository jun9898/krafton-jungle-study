import sys
from collections import deque

input = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def puyo(puyo_arr):
    for y, x in puyo_arr:
        graph[y][x] = "."

def puyo_puyo():
    for x in range(6):
        queue = deque()
        for y in range(11, -1, -1):
            if graph[y][x] != ".":
                queue.append(graph[y][x])
        for y in range(11, -1, -1):
            if queue:
                graph[y][x] = queue.popleft()
            else:
                graph[y][x] = "."

def bfs(y, x, color):
    queue = deque([(y, x)])
    puyo_arr = [(y, x)]
    visited = set([(y, x)])

    while queue:
        cur_y, cur_x = queue.popleft()
        for i in range(4):
            new_y, new_x = cur_y + dy[i], cur_x + dx[i]
            if (
                    0 <= new_y < 12
                    and 0 <= new_x < 6
                    and (new_y, new_x) not in visited
                    and graph[new_y][new_x] == color
            ):
                queue.append((new_y, new_x))
                visited.add((new_y, new_x))
                puyo_arr.append((new_y, new_x))

    if len(puyo_arr) >= 4:
        puyo(puyo_arr)
        return True
    return False

graph = [list(input().rstrip()) for _ in range(12)]
chain = 0

while True:
    exploded = False
    for i in range(12):
        for j in range(6):
            if graph[i][j] != ".":
                if bfs(i, j, graph[i][j]):
                    exploded = True

    if not exploded:
        break

    puyo_puyo()
    chain += 1

print(chain)
