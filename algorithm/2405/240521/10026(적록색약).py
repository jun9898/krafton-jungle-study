from collections import deque


def BFS(x,y):
    q.append((x,y))
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 인덱스 범위 안에 있으면서, 같은 색이면서, 방문 안한 경우
            if 0<=nx<N and 0<=ny<N and a[nx][ny] == a[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1  # 방문체크 후 큐에 넣음
                q.append((nx,ny))


N = int(input())
a = [list(input()) for _ in range(N)]
q = deque()

# 적록색약 아닌 경우
visited = [[0] * N for _ in range(N)]
cnt1 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:  # 아직 방문 안한 경우만 체킹
            BFS(i,j)
            cnt1 += 1

# 적록색약인 경우
for i in range(N):
    for j in range(N):
        if a[i][j] == 'G':
            a[i][j] = 'R'

visited = [[0] * N for _ in range(N)]
cnt2 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(i,j)
            cnt2 += 1

print(cnt1, cnt2)

