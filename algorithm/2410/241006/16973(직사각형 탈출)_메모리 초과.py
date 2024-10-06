import sys
from collections import deque

input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def check(cur_squire, dist, step):
    tmp_square = []
    is_valid = True
    for y, x in cur_squire:
        new_y, new_x = y + dy[dist], x + dx[dist]
        if 0 <= new_y < n and 0 <= new_x < m and graph[new_y][new_x] == 0:
            tmp_square.append((new_y, new_x))
        else:
            is_valid = False
    return is_valid, tmp_square

def bfs():
    queue = deque([(original_square, 0)])
    visited = set()
    while queue:
        cur_square, step = queue.popleft()
        for i in range(4):
            valid, tmp_squire = check(cur_square, i, step)
            if valid and tuple(tmp_squire) not in visited:
                if (FH, FW) == tmp_squire[0]:
                    return step + 1
                queue.append((tmp_squire, step + 1))
                visited.add(tuple(tmp_squire))
    return -1

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

H, W, SH, SW, FH, FW = map(lambda x: x - 1, map(int, input().split()))

original_square = []

for i in range(H + 1):
    for j in range(W + 1):
        original_square.append((SH + i, SW + j))

print(bfs())





