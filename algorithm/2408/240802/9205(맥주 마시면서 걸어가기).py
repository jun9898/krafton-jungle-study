import sys
from collections import deque

input = sys.stdin.readline

def can_reach(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1]) <= 1000

def bfs(start, end, stores):
    queue = deque([start])
    visited = set([start])

    while queue:
        curY, curX = queue.popleft()
        # 애초에 도착할 수 있다면 바로 happy
        if can_reach((curY, curX), end):
            return "happy"


        # 아니면 편의점까지 도달할 수 있는지 체크
        for store in stores:
            if store not in visited and can_reach((curY, curX), store):
                # 도달할 수 있다면 queue에 추가하고 다리 can_reach
                visited.add(store)
                queue.append(store)

    return "sad"

T = int(input())

for _ in range(T):
    n = int(input())
    start = tuple(map(int, input().split()))
    stores = [tuple(map(int, input().split())) for _ in range(n)]
    end = tuple(map(int, input().split()))

    print(bfs(start, end, stores))
