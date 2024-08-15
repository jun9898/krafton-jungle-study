import sys
from collections import deque
from collections import defaultdict

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

input = sys.stdin.readline

'''
약간 불켜기와 비슷한 문제인것같은

가장자리의 모든 좌표를 queue에 집어넣어두고 시작
소유하고 있는 key를 set 자료형에 집어넣기
door는 key : (좌표), (좌표) 이런식으로 저장될것

평상시처럼 탐색.
    만약 문을 찾으면
        가지고 있는 key가 해당 문을 열 수 있는지 확인
        없으면 door에 좌표와 필요한 key를 저장
    만약 key를 찾으면
        key를 set 자료형에 집어넣기
        소유중인 door중에 문을 열 수 있는 위치가 있는지 확인
        만약 열수있다면 
            queue에 열린 문을 집어넣고 visited 처리
        new 좌표 queue에 넣고 계속 탐색
'''
def unlock(queue, key, door, visited):
    for i in key:
        upper_key = i.upper()
        # door에 해당 키가 있는지 확인
        if upper_key in door:
            # 해당 키로 열 수 있는 모든 문의 위치를 순회
            for j in door[upper_key]:
                if j not in visited:
                    queue.append(j)
                    visited.add(j)



def bfs(queue, key, door):
    visited = set(queue)
    unlock(queue, key, door, visited)
    result = 0
    while queue:
        curY, curX = queue.pop()
        if graph[curY][curX] == "$":
            result += 1
        for i in range(4):
            newY, newX = curY + dy[i], curX + dx[i]
            # 유효!
            if 0 <= newY < y and 0 <= newX < x and (newY, newX) not in visited and graph[newY][newX] != "*":
                if graph[newY][newX].isupper():
                    door[graph[newY][newX]].append((newY, newX))
                else:
                    if graph[newY][newX].islower():
                        key.add(graph[newY][newX])
                    visited.add((newY, newX))
                    queue.append((newY, newX))
        unlock(queue, key, door, visited)
    return result








t = int(input())

for _ in range(t):
    y, x = map(int, input().split())
    graph = []
    queue = deque()
    key = set()
    door = defaultdict(list)
    result = 0
    for i in range(y):
        tmpGraph = list(input().rstrip())
        for j in range(x):
            # 가장자리일때
            if (
                (i == 0 or i == y - 1 or j == 0  or j == x - 1) and
                # 벽이 아니고
                tmpGraph[j] != "*"
            ):
                # 자물쇠라면
                if tmpGraph[j].isupper():
                    door[tmpGraph[j]].append((i, j))
                # key라면

                else:
                    if tmpGraph[j].islower():
                        key.add(tmpGraph[j])
                    queue.append((i, j))
        graph.append(tmpGraph)
    keys = set(list(input().rstrip()))
    key = key.union(keys)
    print(bfs(queue, key, door))



