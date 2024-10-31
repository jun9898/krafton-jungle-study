import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
start, end, result = 0, 0, 0
visited = set()

while start <= end and end < n:
    if arr[end] not in visited:
        visited.add(arr[end])
        end += 1
        result += end - start
    else:
        while arr[end] in visited:
            visited.remove(arr[start])
            start += 1

print(result)