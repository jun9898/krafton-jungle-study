import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(y,x):
    queue = deque()
    queue.append((y,x))
    visited[y][x] = 1
    count = 1
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == -1 and plate[ny][nx] == "1":
                queue.append((ny, nx))
                count += 1
                visited[ny][nx] = 1
    result.append(count)


n = int(input())

plate = []

visited = [[-1] * n for _ in range(n)]
result = []

for i in range(n):
    row = input().rstrip()
    plate.append(row)

for i in range(n):
    for j in range(n):
        # 만약 가구가 존재하고 아직 방문하지 않았으면
        if plate[i][j] == "1" and visited[i][j] == -1:
            bfs(i,j)

result.sort()
print(len(result))
for i in result:
    print(i)

