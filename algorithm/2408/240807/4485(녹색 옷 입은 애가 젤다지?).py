import math
import sys
import heapq

input = sys.stdin.readline
INF = math.inf

'''
모든 경로가 가지고 있는 값을 최신화

모든 경로의 경우의수를 계산해야함 (다익스트라)
하지만 모든 노드의 간선을 graph화 하면 메모리 낭비 장난 아닐듯
heapq 쓰면 해결
'''
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    # heapq 생성 (간선 가중치, 좌표)
    heap = []
    heapq.heappush(heap, (graph[0][0], 0, 0))
    while heap:
        curDist, curY, curX = heapq.heappop(heap)
        if curY == n - 1 and curX == n - 1:
            return dist[curY][curX]
        for i in range(4):
            newY, newX = curY + dy[i], curX + dx[i]
            if 0 <= newY < n and 0 <= newX < n:
                newDist = curDist + graph[newY][newX]
                if newDist < dist[newY][newX]:
                    dist[newY][newX] = newDist
                    heapq.heappush(heap, (newDist, newY, newX))


problem = 1
while True:
    n = int(input())
    if n == 0: break
    graph = [list(map(int, input().split())) for _ in range(n)]
    dist = [[INF] * n for _ in range(n)]
    dist[0][0] = graph[0][0]
    print(f'Problem {problem}: {bfs()}')
    problem += 1


