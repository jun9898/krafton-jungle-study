import sys
input = sys.stdin.readline

def bineary_search(arr):
    start, end = 1, max(arr)
    while start <= end:
        # 중간값
        mid = (start + end) // 2
        result = 0
        for value in arr:
            if value - mid >= 0:
                result += value - mid
        if result < m:
            end = mid - 1
        else:
            start = mid + 1
    return end

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = bineary_search(arr)

print(result)

