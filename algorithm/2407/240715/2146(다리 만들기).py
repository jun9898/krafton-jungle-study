import sys
from collections import deque
input = sys.stdin.readline

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


# 우선 각 섬마다 번호표를 붙혀야할 것 같음
# BFS를 2번 돌려서 섬의 갯수와 각각의 섬에 마킹을 해줌
def marking(y, x, mark):
    queue = deque([(y, x)])
    graph[y][x] = mark
    while queue:
        cur_y, cur_x = queue.popleft()
        for i in range(4):
            new_y, new_x = cur_y + dy[i], cur_x + dx[i]
            if 0 <= new_y < n and 0 <= new_x < n and (new_y, new_x) not in visited and graph[new_y][new_x] != 0:
                graph[new_y][new_x] = num
                queue.append((new_y, new_x))
                visited.add((new_y, new_x))


def search(mark):
    queue = deque()
    dist = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == mark:
                queue.append((i, j))
                dist[i][j] = 0

    while queue:
        cur_y, cur_x = queue.popleft()
        for i in range(4):
            new_y, new_x = cur_y + dy[i], cur_x + dx[i]
            if 0 <= new_y < n and 0 <= new_x < n:
                if graph[new_y][new_x] != mark and graph[new_y][new_x] != 0:
                    return dist[cur_y][cur_x]
                if graph[new_y][new_x] == 0 and dist[new_y][new_x] == -1:
                    dist[new_y][new_x] = dist[cur_y][cur_x] + 1
                    queue.append((new_y, new_x))


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = set()
num = 1
for y in range(n):
    for x in range(n):
        if (y, x) not in visited and graph[y][x] != 0:
            visited.add((y, x))
            marking(y, x, num)
            num += 1

result = float("INF")
for i in range(1, num):
    result = min(result, search(i))

print(result)

