import sys
from collections import deque

input = sys.stdin.readline

'''
이 문제의 핵심은 한 방향으로 끝까지 이동해야한다는것
visited 체크는 R, B의 위치를 모두 체크해야할듯
count = 0
while queue
    for _ in range(len(queue)):
        cur location = queue.popleft()
        if count > 10:
            break
        if cur location == 구멍
            return count
        for i in range(4)
            빨간구슬 움직이기
            new location = cur location 현재 위치 복사
            while Ture
                new location += dy[i], dx[i]
                if graph[new location] == "#" 벽이라면
                    new location -= dy[i], dx[i]
                    break
                if graph[new location] == "O" 구멍이라면
                    break
            파란구슬 움직이기 똑같이
            파란구슬이 구멍에 들어가면 꽝
            if graph[blue location] == "O"
                break
            if 여기서 구슬이 겹쳤을때 어떻게 처리할지 생각해봐야함
                구슬 겹친거 정렬하기
            if (new location, new location) not in visited:
                queue.append((new location, new location))
                visited.add((new location, new location))
    
'''

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((redY, redX, blueY, blueX))
    visited = {(redY, redX, blueY, blueX)}
    count = 0
    while queue:
        for _ in range(len(queue)):
            curRedY, curRedX, curBlueY, curBlueX = queue.popleft()
            if count > 10:
                return -1
            if graph[curRedY][curRedX] == 'O':
                return count
            for i in range(4):
                # Red와 Blue 구슬 이동
                newRedY, newRedX = curRedY, curRedX
                newBlueY, newBlueX = curBlueY, curBlueX
                while True:
                    newRedY, newRedX = newRedY + dy[i], newRedX + dx[i]
                    # 벽이면 끝까지 이동했음으로 break
                    if graph[newRedY][newRedX] == '#':
                        newRedY -= dy[i]
                        newRedX -= dx[i]
                        break
                    # 탈출 조건에 부합했음으로 break
                    if graph[newRedY][newRedX] == 'O':
                        break
                # 파란구슬도 동시에 연산
                while True:
                    newBlueY, newBlueX = newBlueY + dy[i], newBlueX + dx[i]
                    # 벽이면 끝까지 이동했음으로 break
                    if graph[newBlueY][newBlueX] == '#':
                        newBlueY -= dy[i]
                        newBlueX -= dx[i]
                        break
                    # 탈출 조건에 부합했음으로 break
                    if graph[newBlueY][newBlueX] == 'O':
                        break
                # 동시에 들어가면 꽝이여
                if graph[newBlueY][newBlueX] == 'O':
                    continue
                # 두 구슬이 겹쳤다면
                if (newRedY, newRedX) == (newBlueY, newBlueX):
                    if abs(curRedY - newRedY) + abs(curRedX - newRedX) > abs(newBlueY - curBlueY) + abs(newBlueX - curBlueX):
                        newRedY -= dy[i]
                        newRedX -= dx[i]
                    else:
                        newBlueY -= dy[i]
                        newBlueX -= dx[i]
                if (newRedY, newRedX, newBlueY, newBlueX) not in visited:
                    queue.append((newRedY, newRedX, newBlueY, newBlueX))
                    visited.add((newRedY, newRedX, newBlueY, newBlueX))
        count += 1
    return -1


n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == "R":
            redY, redX = i, j
        elif graph[i][j] == "B":
            blueY, blueX = i, j

print(bfs())


