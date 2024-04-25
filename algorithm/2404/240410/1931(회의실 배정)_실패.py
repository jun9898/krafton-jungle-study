import sys
import heapq
input = sys.stdin.readline

n = int(input())
max_distance = 0
room = []

for i in range(n):
    start, end = map(int, input().split())
    distance = end - start
    max_distance = max(max_distance, end)
    heapq.heappush(room, (distance, start, end))

visited = [0] * (max_distance + 1)

res = 0
while room:
    distance, start, end = heapq.heappop(room)
    if start == end:
        if visited[start] == 1:
            continue
        else:
            visited[start] = 1
            res += 1
            continue
    for i in range(start, end):
        if visited[i] == 1:
            break
    else:
        for i in range(start, end):
            visited[i] = 1
        res += 1

print(res)