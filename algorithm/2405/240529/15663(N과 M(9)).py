import sys
from collections import defaultdict
input = sys.stdin.readline

result = []


def dfs(cur_arr, n, m):
    tmp = tuple(cur_arr)
    if tmp in visited:
        return
    if len(cur_arr) == m:
        visited.add(tmp)
        result.append(cur_arr[:])
        return
    for i in range(0, n):
        if len(cur_arr) != 0 and arr_dict[arr[i]] == 0:
            continue
        cur_arr.append(arr[i])
        arr_dict[arr[i]] -= 1
        dfs(cur_arr, n, m)
        arr_dict[arr[i]] += 1
        cur_arr.pop()


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

arr_dict = defaultdict(int)
for i in arr:
    arr_dict[i] += 1

visited = set()

dfs([], n, m)

for seq in result:
    print(' '.join(map(str, seq)))
