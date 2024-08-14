import sys
from collections import deque

input = sys.stdin.readline

'''
벽부 2에다가 낮, 밤 하나만 추가하면 될듯
'''

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(k):
    queue = deque([(k, 0, 0, 1, True)])  # k, y, x, time, is_day
    visited[0][0][k] = 1

    while queue:
        curK, curY, curX, time, is_day = queue.popleft()

        if curY == n - 1 and curX == m - 1:
            print(time)
            sys.exit()

        for i in range(4):
            newY, newX = curY + dy[i], curX + dx[i]
            if 0 <= newY < n and 0 <= newX < m:
                if graph[newY][newX] == '0':
                    if visited[newY][newX][curK] == 0:
                        visited[newY][newX][curK] = 1
                        queue.append((curK, newY, newX, time + 1, not is_day))
                elif curK > 0:
                    if is_day and visited[newY][newX][curK - 1] == 0:
                        visited[newY][newX][curK - 1] = 1
                        queue.append((curK - 1, newY, newX, time + 1, not is_day))
                    elif not is_day:
                        queue.append((curK, curY, curX, time + 1, not is_day))

    print(-1)

n, m, k = map(int, input().split())
graph = [input().rstrip() for _ in range(n)]
visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]

bfs(k)
