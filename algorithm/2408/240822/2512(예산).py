import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

start, end = 0, max(arr)


while start <= end:
    pivot = (start + end) // 2
    result = 0
    for i in arr:
        if i > pivot:
            result += pivot
        else:
            result += i
    if result <= m:
        start = pivot + 1
    else:
        end = pivot - 1
print(end)
