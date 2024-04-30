import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(arr, visited, x, y):
    count = 0
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        if (x, y) in visited or arr[y][x] == 0:
            continue
        visited.add((x, y))
        for i in range(4):
            new_x, new_y = x + dx[i], y+dy[i]
            if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in visited:
                queue.append((new_x, new_y))
        count += 1
    return count


t = int(input())


for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    visited = set()
    res = 0
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    for i in range(n):
        for j in range(m):
            if bfs(arr, visited, j, i) != 0:
                res += 1
    print(res)

