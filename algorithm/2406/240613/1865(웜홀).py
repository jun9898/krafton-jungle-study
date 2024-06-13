import sys
input = sys.stdin.readline
inf = int(1e9)

def bellman_ford(start, n):
    distance = [inf for _ in range(n + 1)]
    distance[start] = 0
    for i in range(n):
        for cur_node, next_node, edge_cost in edges:
            if distance[next_node] > distance[cur_node] + edge_cost:
                if i == n - 1:
                    return True
                distance[next_node] = distance[cur_node] + edge_cost
    return False

T = int(input())

for i in range(T):
    N, M, W = map(int, input().split())
    edges = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        edges.append([a, b, c])
        edges.append([b, a, c])
    for _ in range(W):
        a, b, c = map(int, input().split())
        edges.append([a, b, -c])

    negative_cycle = bellman_ford(1, N)

    if negative_cycle:
        print("YES")
    else:
        print("NO")






