import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr_dp = [1] * n

for i in range(1,n):
    for j in range(i):
        if arr[i] > arr[j]:
            arr_dp[i] = max(arr_dp[i], arr_dp[j]+1)

print(max(arr_dp))