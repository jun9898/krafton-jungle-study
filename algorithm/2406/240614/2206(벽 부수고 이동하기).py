import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(y, x, z):
    queue = deque([(y, x, z)])
    while queue:
        cur_y, cur_x, curBreakCount = queue.popleft()
        if cur_y == n - 1 and cur_x == m - 1:
            return visited[cur_y][cur_x][curBreakCount]
        for i in range(4):
            new_y, new_x = cur_y + dy[i], cur_x + dx[i]
            if 0 <= new_y < n and 0 <= new_x < m:
                if graph[new_y][new_x] == "1" and curBreakCount == 0:
                    visited[new_y][new_x][1] = visited[cur_y][cur_x][0] + 1
                    queue.append((new_y, new_x, 1))
                elif graph[new_y][new_x] == "0" and visited[new_y][new_x][curBreakCount] == 0:
                    visited[new_y][new_x][curBreakCount] = visited[cur_y][cur_x][curBreakCount] + 1
                    queue.append((new_y, new_x, curBreakCount))
    return -1


n, m = map(int, input().split())
result = [[0] * m for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

graph = []
for _ in range(n):
    graph.append(list(input().rstrip()))

print(bfs(0, 0, 0))
