import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, -2, -1, -2, 1, 2, 1, 2]
dy = [2, 1, -2, -1, 2, 1, -1, -2]


def bfs(start_y, start_x, dest_y, dest_x):
    queue = deque()
    queue.append((start_y, start_x))
    arr[start_y][start_x] = 1
    while queue:
        cur_y, cur_x = queue.popleft()
        if cur_y == dest_y and cur_x == dest_x:
            return arr[cur_x][cur_y] - 1
        for i in range(8):
            new_y, new_x = cur_y + dy[i], cur_x + dx[i]
            if 0 <= new_y < tmp and 0 <= new_x < tmp:
                if arr[new_y][new_x] == 0:
                    queue.append((new_y, new_x))
                    arr[new_y][new_x] = arr[cur_y][cur_x] + 1


n = int(input())

for i in range(n):
    tmp = int(input())
    start_y, start_x = map(int, input().split())
    dest_y, dest_x = map(int, input().split())
    arr = [[0] * tmp for _ in range(tmp)]
    print(bfs(start_y, start_x, dest_y, dest_x))
