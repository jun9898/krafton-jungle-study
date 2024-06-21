import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
counter = [0] * (max(arr) + 1)
max_len = 0
left, right = 0, 0

while right < n:
    if counter[arr[right]] < m:
        counter[arr[right]] += 1
        right += 1
    else:
        counter[arr[left]] -= 1
        left += 1
    max_len = max(max_len, right - left)

print(max_len)


