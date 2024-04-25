import sys
input = sys.stdin.readline


def binary_search(start, end):
    min = sys.maxsize
    while start < end:
        tmp = arr[start] + arr[end]
        if tmp == 0:
            return arr[start], arr[end]
        if abs(tmp) < min:
            min = abs(tmp)
            answer = arr[start], arr[end]
        if tmp < 0:
            start += 1
        else:
            end -= 1
    return answer


n = int(input())
arr = list(map(int, input().split()))
arr.sort()


result_arr = []
print(*binary_search(0,n-1))




