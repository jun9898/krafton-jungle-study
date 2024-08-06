import sys
from collections import defaultdict, deque

input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

'''
베시시

visited를 처리하는 graph와 불의 현황을 저장하는 graph 두개가 필요함.
우선 visited에 방문을 표시하고 만약 불이 켜져있다면 queue.append

필요한 자료구조.
현재 탐색을 진행할 queue.
방문 처리와 불이 켜진 위치를 저장할 graph 2개
스위치의 위치와 어떤 방 불을 킬 수 있을지 저장할 dict 하나

이렇게 bfs
'''

def bfs():
    queue = deque([(1, 1)])
    visited[1][1] = True
    turnOn[1][1] = True
    result.add((1, 1))

    while queue:
        curY, curX = queue.popleft()

        for _Y, _X in switch[(curY, curX)]:
            # 아직 불이 다 켜지지 않았다면
            if not turnOn[_Y][_X]:
                # 불 다 켜버리기
                turnOn[_Y][_X] = True
                result.add((_Y, _X))
                # 불을 킨곳이 이동 가능하다면
                if visited[_Y][_X]:
                    queue.append((_Y, _X))

        # 탐색 시작
        for i in range(4):
            newY, newX = curY + dy[i], curX + dx[i]
            if 0 < newY <= n and 0 < newX <= n and not visited[newY][newX]:
                visited[newY][newX] = True
                # 이동할때도 한번 더 필터링
                if turnOn[newY][newX]:
                    queue.append((newY, newX))


n, m = map(int, input().split())

visited = [[False for _ in range(n + 1)] for _ in range(n + 1)]
turnOn= [[False for _ in range(n + 1)] for _ in range(n + 1)]
result = set()

switch = defaultdict(list)

for i in range(m):
    y, x, a, b = map(int, input().split())
    switch[(y, x)].append((a, b))

bfs()

print(len(result))


