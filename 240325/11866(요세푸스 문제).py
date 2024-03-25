import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [x for x in range(1, n+1)]
result = []
m = m-1
reset = m

while arr:
    result.append(arr.pop(m))
    m += reset
    if m >= len(arr) and len(arr) != 0:
        m = m % len(arr)

result_str = "<" + ", ".join(str(num) for num in result) + ">"
print(result_str)

