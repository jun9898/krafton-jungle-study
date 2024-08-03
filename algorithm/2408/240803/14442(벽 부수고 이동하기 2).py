import sys
from collections import deque

input = sys.stdin.readline

'''
벽 부수고 이동하기!

graph를 3차원으로 접근하면 되지 않을까
queue에 집어넣는 값을 (y, x, K, count) 이렇게 넣고 K가 0이 되거나 y, x가 유효하지 않은 범위에 들어가면 안넣기
그렇게 가장 빨리 도착하게 되는 값의 count를 print
'''

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(K):
    # y, x, count, K
    queue = deque([(K, 0, 0)])
    visited[0][0][K] = 1
    while queue:
        curK, curY, curX  = queue.popleft()
        if curY == N-1 and curX == M-1:
            print(visited[curY][curX][curK])
            return
        for i in range(4):
            newY, newX = curY + dy[i], curX + dx[i]
            # 유효!
            if 0 <= newY < N and 0 <= newX < M:
                # 벽인가 아닌가
                if graph[newY][newX] == 0 and visited[newY][newX][curK] == 0:
                    visited[newY][newX][curK] = visited[curY][curX][curK] + 1
                    queue.append((curK, newY, newX))
                # 벽을 부술 수 있다면
                elif graph[newY][newX] == 1 and curK > 0 and visited[newY][newX][curK - 1] == 0:
                    visited[newY][newX][curK - 1] = visited[curY][curX][curK] + 1
                    queue.append((curK - 1, newY, newX))


    print(-1)
    return


N, M, K = map(int, input().split())

graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0]*(K+1) for _ in range(M)] for __ in range(N)]
bfs(K)

