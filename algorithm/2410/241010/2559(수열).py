import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

window = sum(arr[:k])
result = window

for i in range(k, n):
    window += (arr[i] - arr[i - k])
    result = max(result, window)

print(result)

