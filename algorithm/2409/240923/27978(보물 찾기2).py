import sys
import heapq

input = sys.stdin.readline

# 순풍: 동, 북동, 남동
# 역풍: 서, 북서, 남서, 북, 남
dy = [0, -1, 1, 0, -1, 1, -1, 1]
dx = [1, 1, 1, -1, -1, -1, 0, 0]

def dijkstra(start_y, start_x):
    queue = [(0, start_y, start_x)]
    dist = [[float('inf')] * w for _ in range(h)]
    dist[start_y][start_x] = 0

    while queue:
        time, cur_y, cur_x = heapq.heappop(queue)

        if graph[cur_y][cur_x] == '*':
            return time

        if time > dist[cur_y][cur_x]:
            continue

        for i in range(8):
            ny, nx = cur_y + dy[i], cur_x + dx[i]

            if 0 <= ny < h and 0 <= nx < w and graph[ny][nx] != '#':
                new_time = time if i < 3 else time + 1
                if new_time < dist[ny][nx]:
                    dist[ny][nx] = new_time
                    heapq.heappush(queue, (new_time, ny, nx))

    return -1

h, w = map(int, input().split())
graph = [list(input().strip()) for _ in range(h)]

start_y, start_x = next((i, j) for i in range(h) for j in range(w) if graph[i][j] == 'K')

print(dijkstra(start_y, start_x))
