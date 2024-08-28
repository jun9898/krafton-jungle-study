import sys
input = sys.stdin.readline

def dfs(tmp_arr, index):
    if len(tmp_arr) == m and tuple(tmp_arr) not in visited:
        visited.add(tuple(tmp_arr))
        print(*tmp_arr)
        return
    for i in range(index, n):
        tmp_arr.append(arr[i])
        dfs(tmp_arr, i + 1)
        tmp_arr.pop()

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
visited = set()

dfs([], 0)

