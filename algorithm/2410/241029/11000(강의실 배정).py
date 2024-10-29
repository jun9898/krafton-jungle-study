import sys
import heapq

input = sys.stdin.readline

N = int(input())
events = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: (x[0], x[1]))

end_times = [events[0][1]]
for i in range(1, N):
    if end_times[0] <= events[i][0]:
        heapq.heapreplace(end_times, events[i][1])
    else:
        heapq.heappush(end_times, events[i][1])

print(len(end_times))