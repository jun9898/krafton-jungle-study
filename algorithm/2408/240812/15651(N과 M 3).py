import sys
input = sys.stdin.readline

def dfs(arr, n, m):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(1, n + 1):
        arr.append(i)
        dfs(arr, n, m)
        arr.pop()


n, m = map(int, input().split())
dfs([], n, m)

