import sys
input = sys.stdin.readline

result = []


def dfs(cur_arr, start, n, m):
    if len(cur_arr) == m:
        result.append(cur_arr[:])
        return
    for i in range(start, n + 1):
        cur_arr.append(i)
        dfs(cur_arr, i + 1, n, m)
        cur_arr.pop()


n, m = map(int, input().split())
dfs([], 1, n, m)

# 결과 출력
for seq in result:
    print(' '.join(map(str, seq)))
