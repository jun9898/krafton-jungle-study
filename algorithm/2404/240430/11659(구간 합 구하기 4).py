import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
tmp_arr = [0]

for i in arr:
    tmp_arr.append(tmp_arr[-1] + i)

for i in range(m):
    tmp1, tmp2 = map(int, input().split())
    print(tmp_arr[tmp2] - tmp_arr[tmp1-1])
