import sys
from collections import deque
input = sys.stdin.readline
INF = float('-inf')

'''
결국 bfs + 비트마스킹을 응용하면 되는 문제였음
문제를 이해하기까진 어려웠지만 이해 후엔 그냥 무지성 bf랑 똑같았음
'''

def bfs(N, initialPositions):
    distance = [INF] * (N + 1)
    # BFS 큐 초기화
    queue = deque()
    # 초기 위치 설정
    for position in initialPositions:
        distance[position] = 0
        queue.append(position)

    maxDistance = 0

    while queue:
        current = queue.popleft()
        for bit in range(20):
            nextPosition = current ^ (1 << bit)
            if nextPosition > N or distance[nextPosition] != INF:
                continue
            queue.append(nextPosition)
            distance[nextPosition] = distance[current] + 1
            maxDistance = max(maxDistance, distance[nextPosition])

    return maxDistance

N = int(input())
M = int(input())
initial_positions = list(map(int, input().split()))

result = bfs(N, initial_positions)
print(result)