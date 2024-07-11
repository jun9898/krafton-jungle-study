import sys
input = sys.stdin.readline

N = int(input())
building = []

for i in range(N):
    building.append(int(input()))

stack = []
result = 0

for b in building:
    while stack and stack[-1] <= b:
        stack.pop()
    stack.append(b)
    result += len(stack) - 1

print(result)