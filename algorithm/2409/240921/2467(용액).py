import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

start_index = 0
end_index = n - 1
solution = float('inf')

while start_index < end_index:
    tmp = arr[start_index] + arr[end_index]
    if abs(tmp) < solution:
        result = (arr[start_index], arr[end_index])
        solution = abs(tmp)
        if solution == 0:
            break
    if tmp < 0:
        start_index += 1
    elif tmp > 0:
        end_index -= 1

print(*result)



