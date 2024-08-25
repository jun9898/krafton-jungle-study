import sys
input = sys.stdin.readline

def dfs(tmp_arr, index):
    if len(tmp_arr) == m:
        print(*tmp_arr)
        return
    for i in range(index, n):
        tmp_arr.append(arr[i])
        dfs(tmp_arr, i + 1)
        tmp_arr.pop()


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

dfs([], 0)

