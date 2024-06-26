import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(y, x, result):
    visited.add((y, x))
    queue = deque([(y, x)])
    while queue:
        cur_y, cur_x = queue.popleft()
        for i in range(4):
            new_y, new_x = cur_y + dy[i], cur_x + dx[i]
            if 0 <= new_y < n and 0 <= new_x < m  and (new_y, new_x) not in visited and arr[new_y][new_x] == 1:
                visited.add((new_y, new_x))
                queue.append((new_y, new_x))
                result += 1
    return result

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

visited = set()

result = []
for i in range(n):
    for j in range(m):
        if (i, j) not in visited and arr[i][j] == 1:
            result.append(bfs(i, j, 1))

print(len(result))
if len(result) != 0:
    print(max(result))
else:
    print(0)

