import sys
import math
input = sys.stdin.readline

n = int(input())

inf = math.inf

container = []

for i in range(n):
    row = list(map(int, input().split()))
    container.append(row)

dp = [[-1] * (1 << n) for _ in range(n)]


def dfs(start, visited):
    # 탈출조건
    if visited == (1 << n)-1:
        if container[start][0]:
            return container[start][0]
        else:
            return inf

    if dp[start][visited] != -1:
        return dp[start][visited]

    min_val = inf
    # DP 조건
    for next in range(1, n):
        # 이미 방문 했거나 연결되어있지 않으면
        if container[start][next] == 0 or visited & (1 << next):
            continue
        cost = dfs(next, visited | (1 << next)) + container[start][next]
        min_val = min(min_val, cost)

    dp[start][visited] = min_val
    return min_val


print(dfs(0, 1))