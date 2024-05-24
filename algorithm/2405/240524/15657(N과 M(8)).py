import sys
input = sys.stdin.readline

result = []


def dfs(cur_arr, n, m):
    if len(cur_arr) == m:
        result.append(cur_arr[:])
        return
    for i in range(0, n):
        if len(cur_arr) != 0 and arr[i] < cur_arr[-1]:
            continue
        cur_arr.append(arr[i])
        dfs(cur_arr, n, m)
        cur_arr.pop()


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

dfs([], n, m)

for seq in result:
    print(' '.join(map(str, seq)))
