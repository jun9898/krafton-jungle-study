import sys
from collections import deque

input = sys.stdin.readline

next_directions = {
    0: [2, 3],  # 동쪽에서는 북쪽이나 남쪽으로
    1: [2, 3],  # 서쪽에서는 북쪽이나 남쪽으로
    2: [0, 1],  # 북쪽에서는 동쪽이나 서쪽으로
    3: [0, 1]   # 남쪽에서는 동쪽이나 서쪽으로
}


def bfs():
    queue = deque([(startY, startX, startD, 0)])
    visited = set([(startY, startX, startD)])
    while queue:
        curY, curX, curD, step = queue.popleft()
        if curY == endY and curX == endX and curD == endD:
            return step
        # 현재 방향으로 1, 2, 3칸 이동
        for i in range(1, 4):
            newY = curY + dy[curD] * i
            newX = curX + dx[curD] * i
            if not (0 <= newY < n and 0 <= newX < m) or graph[newY][newX] == 1:
                break
            if (newY, newX, curD) not in visited:
                visited.add((newY, newX, curD))
                queue.append((newY, newX, curD, step + 1))
        # 90도 회전
        for new_d in next_directions[curD]:
            if (curY, curX, new_d) not in visited:
                visited.add((curY, curX, new_d))
                queue.append((curY, curX, new_d, step + 1))


dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

startY, startX, startD = map(int, input().split())
endY, endX, endD = map(int, input().split())

startY -= 1; startX -= 1; startD -= 1
endY -= 1; endX -= 1; endD -= 1

print(bfs())
