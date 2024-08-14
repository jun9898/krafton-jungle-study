import sys
from collections import deque

'''
벽부 2에다가 낮, 밤 하나만 추가하면 될듯
'''

input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
inf = float('inf')

def bfs(k):
    global result
    queue = deque([(k, 0, 0, 1)])
    visited[0][0][k] = 1
    while queue:
        curK, curY, curX, time = queue.popleft()
        if curY == n - 1 and curX == m - 1:
            print(visited[curY][curX][curK] + 1)
            return
        afternoon = time % 2
        for i in range(4):
            newY, newX = curY + dy[i], curX + dx[i]
            if 0 <= newY < n and 0 <= newX < m:
                if graph[newY][newX] == '0' and visited[newY][newX][curK] > time:
                    visited[newY][newX][curK] = time
                    queue.append((curK, newY, newX, time + 1))
                # 만약 벽을 뚫어야할때 체크해야할것 (curK횟수, 이미 지나간 전적이 있는지)
                elif graph[newY][newX] == '1' and curK > 0 and visited[newY][newX][curK - 1] > time:
                    if afternoon:
                        visited[newY][newX][curK - 1] = time
                        queue.append((curK - 1, newY, newX, time + 1))
                    # 만약 밤이라면
                    else:
                        # 방문 횟수만 늘리기
                        queue.append((curK, curY, curX, time + 1))

    print(-1)
    return

n, m, k = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[[inf] * (k + 1) for _ in range(m)] for __ in range(n)]
bfs(k)
