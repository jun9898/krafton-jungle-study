import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
reverse_arr = list(reversed(arr))

inc = [1 for i in range(n)]
dec = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            inc[i] = max(inc[i], inc[j]+1)
        if reverse_arr[i] > reverse_arr[j]:
            dec[i] = max(dec[i], dec[j]+1)

dec.reverse()

result = 0
for i in range(n):
    result = max(result, inc[i] + dec[i] - 1)

print(result)