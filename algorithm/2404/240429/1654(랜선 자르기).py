# 잘라서 나올 수 있는 가장 근사치를 구하고
def binary_search(arr, start, end):
    while start <= end:
        mid = (start + end) // 2
        tmp = 0
        for i in arr:
            tmp += i // mid
        if tmp >= n:
            # 가장 근사치
            start = mid + 1
        else:
            end = mid - 1
    return end


k, n = map(int, input().split())

arr = []
for i in range(k):
    arr.append(int(input()))

max_arr = max(arr)

print(binary_search(arr, 1, max_arr))
