import sys
from collections import deque
import math
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    queue = deque()
    queue.append((0,0))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            move_to_x = x + dx[i]
            move_to_y = y + dy[i]

            if 0 <= move_to_x < m and 0 <= move_to_y < n and plate[move_to_y][move_to_x] == 1:
                queue.append((move_to_x, move_to_y))
                plate[move_to_y][move_to_x] = plate[y][x] + 1
    return plate[n-1][m-1]



n, m = map(int, input().split())
# 동서남북

result = math.inf

plate = list()
for i in range(n):
    plate.append(list(map(int,input().rstrip())))

res = 0
print(bfs())


