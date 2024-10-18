import sys
input = sys.stdin.readline

n = int(input())
stack = []
result = 0

for _ in range(n):
    height = int(input())

    while stack and stack[-1][0] < height:
        result += stack.pop()[1]

    if not stack:
        stack.append((height, 1))
        continue

    if stack[-1][0] == height:
        count = stack.pop()[1]
        result += count
        if stack:
            result += 1
        stack.append((height, count + 1))
    else:
        stack.append((height, 1))
        result += 1

print(result)
