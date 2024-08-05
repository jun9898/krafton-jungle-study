import sys
from collections import deque

input = sys.stdin.readline

def check(curY, curX, curD, queue, step):
    if 0 <= curD < 2:
        checkStart, checkFinish = 2, 4
    else:
        checkStart, checkFinish = 0, 2
    for i in range(checkStart, checkFinish):
        if (curY, curX, i) not in visited:
            visited.add((curY, curX, i))
            queue.append((curY, curX, i, step + 1))

def bfs():
    # 현재 위치와 방향, 그리고 step
    queue = deque([(startY, startX, startD, 0)])
    visited.add((startY, startX, startD))
    while queue:
        curY, curX, curD, step = queue.popleft()
        if curY == endY and curX == endX and curD == endD:
            print(step)
            return
        # 현재 위치에서 방향으로 전진
        for i in range(1, 4):
            newY = curY + (dy[curD] * i)
            newX = curX + (dx[curD] * i)
            if not (0 <= newY < n and 0 <= newX < m) or graph[newY][newX] == 1:
                break
            if (newY, newX, curD) not in visited:
                visited.add((newY, newX, curD))
                queue.append((newY, newX, curD, step + 1))
        check(curY, curX, curD, queue, step)

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
startY, startX, startD = map(int, input().split())
endY, endX, endD = map(int, input().split())

# 입력된 좌표와 방향을 0부터 시작하는 인덱스로 변환
startY -= 1; startX -= 1; startD -= 1
endY -= 1; endX -= 1; endD -= 1

visited = set()

bfs()
