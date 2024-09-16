import sys
from collections import deque

input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

'''
1. 전체 탐색 후 공기과 접촉하는 부위를 저장
2. 해당 부위의 총 개수 저장
3. 저장해놓은 부위를 다시 queue에 넣고 0으로 변경
'''

def bfs(queue, visited):
    tmp_queue = deque()
    while queue:
        curY, curX = queue.popleft()
        for i in range(4):
            newY, newX = curY + dy[i], curX + dx[i]
            if 0 <= newY < n and 0 <= newX < m and (newY, newX) not in visited:
                if graph[newY][newX] == 0:
                    queue.append((newY, newX))
                elif graph[newY][newX] == 1:
                    tmp_queue.append((newY, newX))
                visited.add((newY, newX))
    return tmp_queue

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

queue = deque([(0, 0)])
visited = {(0, 0)}
result = 0
cheese = 0

while queue:
    tmp_queue = bfs(queue, visited)
    if tmp_queue:
        cheese = len(tmp_queue)
        result += 1
    queue = tmp_queue

print(result)
print(cheese)