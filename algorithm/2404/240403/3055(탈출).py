import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
map = [list(input().rstrip()) for _ in range(r)]

visited = [[-1] * c for _ in range(r)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

q = deque()

for y in range(r):
    for x in range(c):
        if map[y][x] == '*':
            q.appendleft((y, x))
        elif map[y][x] == 'S':
            q.append((y, x))
            visited[y][x] = 0

while q:
    # 최초엔 물을 차게 하고 후에는 고슴도치 이동
    y, x = q.popleft()
    cur = map[y][x]  # 현재 위치
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if ny < 0 or ny >= r or nx < 0 or nx >= c:
            continue
        if visited[ny][nx] != -1:
            continue
        if map[ny][nx] == "*":
            continue
        if map[ny][nx] == "X":
            continue
        if cur == "*" and map[ny][nx] == "D":
            continue
        if cur == "S":
            if map[ny][nx] == "D":  # 고슴이가 가려는 위치가 비버네면 도착
                print(visited[y][x] + 1)
                break
            visited[ny][nx] = visited[y][x] + 1
        map[ny][nx] = cur
        q.append((ny, nx))
    else:
        continue
    break
else:
    print("KAKTUS")
