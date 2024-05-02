import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, visited):
    count = 0
    queue = deque([(x, y)])
    visited.add((x, y))
    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and graph[ny][nx] != "X":
                if graph[ny][nx] == "P":
                    count += 1
                queue.append((nx, ny))
                visited.add((nx, ny))
    return count


n, m = map(int, input().split())
graph = []
start_x, start_y = 0, 0
for i in range(n):
    row = input().rstrip()
    tmp = []
    for j in range(m):
        if "I" == row[j]:
            start_x, start_y = j, i
        tmp.append(row[j])
    graph.append(tmp)

count = bfs(start_x, start_y, set())

if count:
    print(count)
else:
    print("TT")