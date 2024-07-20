import sys
from collections import deque

input = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


# 바이러스 전파 로직
def bfs(virus = deque(), visited = set()):
    # 방문처리를 담당할 set을 선언한 뒤 바이러스의 진원지를 방문처리.
    # 이것도 밖에서 한번 해놓으면 일일히 선언할필요 없지 않을까
    queue = virus.copy()
    cur_visited = visited.copy()

    # 전파 시작
    while queue:
        cur_y, cur_x = queue.popleft()
        for i in range(4):
            new_y, new_x = cur_y + dy[i], cur_x + dx[i]
            if 0 <= new_y < n and 0 <= new_x < m:
                if graph[new_y][new_x] == 0 and (new_y, new_x) not in cur_visited:
                    queue.append((new_y, new_x))
                    cur_visited.add((new_y, new_x))

    # 전파가 끝나고 나면 안전영역 카운트
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0 and (i, j) not in cur_visited:
                count += 1

    return count

# 이제 벽세우는 로직
# 백트레킹을 사용해보자
def dfs(w):
    if w == 3:
        global result
        result = max(result, bfs(virus, visited))
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                dfs(w + 1)
                graph[i][j] = 0


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

virus = deque()
visited = set()
result = 0

# 바이러스의 진원지 파악
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus.append([i, j])
            visited.add((i, j))

dfs(0)
print(result)