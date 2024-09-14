import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
arr.sort()

result = 0

for i in range(n):
    target = arr[i]
    start_index = 0
    # arr에 들어가있는 값이 음수일수도 있음으로 전체 숫자를 탐색해야함
    end_index = len(arr)-1
    while start_index < end_index:
        # 본인은 제외해야함
        if start_index == i:
            start_index += 1
            continue
        if end_index == i:
            end_index -= 1
            continue
        if arr[start_index] + arr[end_index] > target:
            end_index -= 1
        elif arr[start_index] + arr[end_index] < target:
            start_index += 1
        else:
            result += 1
            break

print(result)