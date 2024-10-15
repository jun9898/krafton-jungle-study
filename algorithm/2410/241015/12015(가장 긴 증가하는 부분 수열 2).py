import sys
input = sys.stdin.readline

def binary_search(cur):
    left, right = 0, len(lis) - 1
    while left < right:
        mid = (left + right) // 2
        if lis[mid] < cur:
            left = mid + 1
        else:
            right = mid
    return right

n = int(input())
arr = list(map(int, input().split()))

lis = [arr[0]]

for i in arr:
    if i > lis[-1]:
        lis.append(i)
    else:
        lis[binary_search(i)] = i

print(len(lis))


