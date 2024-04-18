from collections import deque
import sys
input = sys.stdin.readline

# d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
#
#
# def bfs(depth, visited):
#     count = 0
#     for i in range(N):
#         for j in range(N):
#             if not visited[i][j] and Map[i][j] > depth:     # 방문한 적이 없고 안전 영역이라면,
#                 count += 1
#                 queue = deque([(i, j)])                     # 큐에 현재 위치 삽입
#                 visited[i][j] = True                        # & 방문 처리
#
#                 while queue:                                # 큐에 있는 위치들에 대해
#                     x, y = queue.popleft()
#
#                     for k in range(4):                      # 상하좌우 좌표 체크
#                         nx = x + d[k][0]
#                         ny = y + d[k][1]
#
#                         # 만약, 방문한 적이 없고 지도를 벗어나지 않으면서 안전 영역이라면,
#                         if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] is False and Map[nx][ny] > depth:
#                             queue.append((nx, ny))          # 큐에 좌표 삽입
#                             visited[nx][ny] = True          # & 방문 처리
#     return count
#
# N = int(input())
# Map = [list(map(int, input().split())) for _ in range(N)]
#
# max_count = 0
# for depth in range(101):
#     visited = [[False] * N for _ in range(N)]
#     max_count = max(max_count, bfs(depth, visited))
#
# print(max_count)





#
# d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
#
# def search(depth, visited):
#     res = 0
#     for y in range(0, N-1):
#         for x in range(0, N - 1):
#             res += bfs(x,y,visited)
#
#
#
# def bfs(x,y,visited):
#     queue = deque()
#     if (x,y) not in visited:
#         visited.add((x,y))
#         queue.append((x,y))
#         while queue:
#             x,y = queue.popleft()
#             for i in range(4):
#













N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

max_count = 0
for depth in range(101):
    visited = set()
    max_count = max(max_count, search(depth, visited))

print(max_count)












