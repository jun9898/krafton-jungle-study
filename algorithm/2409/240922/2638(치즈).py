import sys
from collections import deque

input = sys.stdin.readline

'''
바깥공기부터 탐색
만약 공기에 노출된 치즈를 발견할시 해당 치즈의 값을 +1
    만약 그렇게 더한 치즈의 숫자가 2 이상일경우 melting cheese에 추가
순회가 끝나면 melting cheese에 담겨있던 치즈를 다 녹인다.
melting cheese를 탐색 queue에 append

여기서 포인트는 melting count를 계속 유지해주며 작업 queue에 더해주는것같음

필요한 자료형
치즈 graph
melting count graph
작업 queue
melting queue
visited
'''
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(queue):
    melting_cheese = deque()
    while queue:
        cur_y, cur_x = queue.popleft()
        for i in range(4):
            new_y, new_x = cur_y + dy[i], cur_x + dx[i]
            if 0 <= new_y < n and 0 <= new_x < m and (new_y, new_x) not in visited:
                if graph[new_y][new_x] == 0:
                    queue.append((new_y, new_x))
                    visited.add((new_y, new_x))
                elif graph[new_y][new_x] == 1:
                    melting_graph[new_y][new_x] += 1
                    if melting_graph[new_y][new_x] >= 2:
                        melting_cheese.append((new_y, new_x))
                        visited.add((new_y, new_x))

    for melt in melting_cheese:
        melt_y, melt_x = melt
        graph[melt_y][melt_x] = 0
        cheese.remove((melt_y, melt_x))

    return melting_cheese

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cheese = set()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cheese.add((i, j))


melting_graph = [[0 for _ in range(m)] for _ in range(n)]
visited = {(0, 0)}
queue = deque([(0, 0)])

result = 0
while cheese:
    queue = bfs(queue)
    result += 1

print(result)



