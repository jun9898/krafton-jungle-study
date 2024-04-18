import sys
import math
import heapq

input = sys.stdin.readline

direction_x = [1, -1, 0, 0]
direction_y = [0, 0, 1, -1]


def make_graph(n):
    graph = [[] for _ in range(n)]
    for i in range(n):
        row = input().rstrip()
        for j in row:
            graph[i].append(int(j))
    return graph


def dijkstar(cost = 0, y = 0, x = 0, visited = set()):
    # 값을 저장할 보드 추가
    check_cost_board = [[math.inf] * n for _ in range(n)]
    check_cost_board[0][0] = 0
    # 우선순위 큐 선언
    pq = []
    heapq.heappush(pq, (cost, y, x))
    while pq:
        cost, y, x = heapq.heappop(pq)
        visited.add((y,x))
        if y == n - 1 and x == n - 1:
            return cost
        for i in range(4):
            nx = x + direction_x[i]
            ny = y + direction_y[i]
            if (ny, nx) in visited:
                continue
            if 0 <= nx < n and 0 <= ny < n and check_cost_board[ny][nx] > cost + 1:
                if graph[ny][nx] == 0:
                    check_cost_board[ny][nx] = cost+1
                    heapq.heappush(pq, (check_cost_board[ny][nx], ny, nx))
                elif graph[ny][nx] == 1:
                    check_cost_board[ny][nx] = cost
                    heapq.heappush(pq, (check_cost_board[ny][nx], ny, nx))


n = int(input())
graph = make_graph(n)
print(dijkstar())



