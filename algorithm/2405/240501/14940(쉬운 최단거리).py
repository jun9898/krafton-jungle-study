import sys
from collections import deque


def bfs(x, y, visited):
    res_arr[y][x] = 0
    q = deque([(x, y)])
    while q:
        cur_x, cur_y = q.popleft()
        if (cur_x, cur_y) in visited or arr[cur_y][cur_x] == 0:
            continue
        visited.add((cur_x, cur_y))
        for i in range(4):
            new_x, new_y = cur_x + dx[i], cur_y + dy[i]
            if (new_x, new_y) in visited or new_x < 0 or new_y < 0 or new_x >= m or new_y >= n:
                continue
            res_arr[new_y][new_x] = res_arr[cur_y][cur_x] + 1
            q.append((new_x, new_y))


input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

arr = []
res_arr = [[-1] * m for _ in range(n)]

start_x, start_y = 0, 0

for i in range(n):
    row = list(map(int, input().split()))
    if 2 in row:
        start_x, start_y = row.index(2), i
    arr.append(row)

bfs(start_x, start_y, set())

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            res_arr[i][j] = 0

for i in res_arr:
    print(*i)



