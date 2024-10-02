import sys
input = sys.stdin.readline

def dfs(arr):
    if len(arr) == n:
        print(*arr)
        return
    for i in range(1, n + 1):
        if i not in visited:
            visited.add(i)
            arr.append(i)
            dfs(arr)
            arr.pop()
            visited.remove(i)

n = int(input())
visited = set()

dfs([])
