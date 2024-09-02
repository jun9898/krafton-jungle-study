import sys
from collections import deque

input = sys.stdin.readline

def dfs(tmp_arr, index, k):
    if len(tmp_arr) == 6:
        print(*tmp_arr)
    for i in range(index, k):
        if not tmp_arr:
            tmp_arr.append(tmp[i])
            dfs(tmp_arr, index + 1, k)
            tmp_arr.pop()
        elif tmp[i] > tmp_arr[-1]:
            tmp_arr.append(tmp[i])
            dfs(tmp_arr, index + 1, k)
            tmp_arr.pop()



while True:
    tmp = deque(map(int, input().split()))
    k = tmp.popleft()
    if k == 0:
        break
    sorted(tmp)
    dfs([], 0, k)
    print()

