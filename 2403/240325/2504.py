import sys
input = sys.stdin.readline

input_string = list(input().rstrip())
tmp = 1
result = 0
stack = []

for i in range(len(input_string)):
    if input_string[i] == "(":
        tmp *= 2
        stack.append(input_string[i])
    elif input_string[i] == "[":
        tmp *= 3
        stack.append(input_string[i])
    elif input_string[i] == ")":
        if len(stack) == 0 or stack[-1] != "(":
            result = 0
            break
        if input_string[i - 1] == "(":
            result += tmp
        stack.pop()
        tmp //= 2
    elif input_string[i] == "]":
        if len(stack) == 0 or stack[-1] != "[":
            result = 0
            break
        if input_string[i - 1] == "[":
            result += tmp
        stack.pop()
        tmp //= 3

if len(stack) != 0:
    print(0)
else:
    print(result)

