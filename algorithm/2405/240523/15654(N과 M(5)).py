import sys
input = sys.stdin.readline

result = []


def dfs(cur_arr, start, n, m):
    if len(cur_arr) == m:
        result.append(cur_arr[:])
        return
    for i in range(0, n):
        if arr[i] in cur_arr:
            continue
        cur_arr.append(arr[i])
        dfs(cur_arr, i + 1, n, m)
        cur_arr.pop()


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

dfs([], 0, n, m)

for seq in result:
    print(' '.join(map(str, seq)))
