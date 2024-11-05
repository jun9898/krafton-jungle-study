import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline


def read_integer_list():
    return list(map(int, input().strip().split()))


def calculate_max_items():
    N, max_distance, road_count = list(map(int, input().split()))
    treasures = list(map(int, input().split()))

    graph = defaultdict(list)
    for _ in range(road_count):
        src, dst, length = list(map(int, input().split()))
        graph[src - 1].append((dst - 1, length))
        graph[dst - 1].append((src - 1, length))

    def dijkstra(start):
        distances = [float('inf')] * N
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_dist, current = heappop(priority_queue)

            if current_dist > distances[current]:
                continue

            for neighbor, weight in graph[current]:
                distance = current_dist + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heappush(priority_queue, (distance, neighbor))

        return distances

    max_collected = 0
    for start_point in range(N):
        shortest_paths = dijkstra(start_point)

        current_collected = sum(
            treasures[i]
            for i in range(N)
            if shortest_paths[i] <= max_distance
        )

        max_collected = max(max_collected, current_collected)

    return max_collected


print(calculate_max_items())