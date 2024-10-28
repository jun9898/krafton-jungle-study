import sys
from collections import deque
input = sys.stdin.readline

dy = [-3, -3, -2, -2, 2, 2, 3, 3]
dx = [-2, 2, -3, 3, -3, 3, -2, 2]

check_y = [
    [-1, -2],
    [-1, -2],
    [0, -1],
    [0, -1],
    [0, 1],
    [0, 1],
    [1, 2],
    [1, 2]
]

check_x = [
    [0, -1],
    [0, 1],
    [-1, -2],
    [1, 2],
    [-1, -2],
    [1, 2],
    [0, -1],
    [0, 1]
]

def point_validator(y, x):
    return 0 <= y < 10 and 0 <= x < 9

def is_valid(cur_y, cur_x, dir):
    for k in range(2):
        mid_y = cur_y + check_y[dir][k]
        mid_x = cur_x + check_x[dir][k]
        if (mid_y, mid_x) == (king_y, king_x):
            return False
    return True

def bfs():
    queue = deque([(start_y, start_x)])
    visited[start_y][start_x] = 0

    while queue:
        cur_y, cur_x = queue.popleft()
        if (cur_y, cur_x) == (king_y, king_x):
            return visited[cur_y][cur_x]

        for i in range(8):
            new_y, new_x = cur_y + dy[i], cur_x + dx[i]
            if point_validator(new_y, new_x) and is_valid(cur_y, cur_x, i) and visited[new_y][new_x] == -1:
                visited[new_y][new_x] = visited[cur_y][cur_x] + 1
                queue.append((new_y, new_x))
    return -1

graph = [[0 for _ in range(9)] for _ in range(10)]
visited = [[-1 for _ in range(9)] for _ in range(10)]

start_y, start_x = map(int, input().split())
king_y, king_x = map(int, input().split())
graph[king_y][king_x] = 1

print(bfs())
