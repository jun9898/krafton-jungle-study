import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
Tomatoes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False] * M for _ in range(N)] for _ in range(H)]
count = 0
queue = deque()

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs():
    while queue:
        z, y, x = queue.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and visited[nz][ny][nx] == 0 and Tomatoes[nz][ny][nx] != -1:
                queue.append((nz, ny, nx))
                Tomatoes[nz][ny][nx] = Tomatoes[z][y][x] + 1
                visited[nz][ny][nx] = True

for i in range(H):
    for j in range(N):
        for k in range(M):
            if Tomatoes[i][j][k] == 1 and visited[i][j][k] == 0:
                queue.append((i, j, k))
                visited[i][j][k] = True

bfs()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if Tomatoes[i][j][k] == 0:
                print(-1)
                quit()
            count = max(count, Tomatoes[i][j][k])

print(count - 1)
