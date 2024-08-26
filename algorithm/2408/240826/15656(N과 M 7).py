import sys
input = sys.stdin.readline

def dfs(tmp_arr):
    if len(tmp_arr) == m:
        print(*tmp_arr)
        return
    for i in range(n):
        tmp_arr.append(arr[i])
        dfs(tmp_arr)
        tmp_arr.pop()


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()


dfs([])