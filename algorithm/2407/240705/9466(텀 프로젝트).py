import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x):
    global n
    visited[x] = True
    cycle.append(x)
    number = numbers[x]

    if visited[number]:
        if number in cycle:
            n -= len(cycle[cycle.index(number):])
        return
    else:
        dfs(number)

t = int(input())

for i in range(t):
    n = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [True] + [False] * n
    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(n)
