import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(cur, cost):
    global visited
    currentLocation = graph[cur]
    currentType = currentLocation[0]
    nextLocation = list(map(int, currentLocation[2:-1]))
    if currentType == "L":
        cost = max(cost, int(currentLocation[1]))
    elif currentType == "T":
        cost -= int(currentLocation[1])
        if cost < 0: return False
    if cur == n:
        return True
    visited.add(cur)
    for nextLo in nextLocation:
        if nextLo not in visited:
            if dfs(nextLo, cost):
                return True
    visited.remove(cur)
    return False


while True:
    n = int(input())
    if n == 0: break
    graph = [()]
    for i in range(n):
        graph.append((input().rstrip().split()))
    visited = set()
    if (dfs(1, 0)):
        print("Yes")
    else:
        print("No")


