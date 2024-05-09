import sys
input = sys.stdin.readline

pipe = list(input().rstrip())

stack = []

res = 0

for i in range(len(pipe)):
    if pipe[i] == '(':
        stack.append(pipe[i])
    else:
        if pipe[i - 1] == "(":
            stack.pop()
            res += len(stack)
        else:
            stack.pop()
            res += 1

print(res)
