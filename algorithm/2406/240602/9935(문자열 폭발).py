import sys
input = sys.stdin.readline

input_string = list(input().rstrip())
sub_string = list(input().rstrip())
total_len = len(input_string)
sub_len = len(sub_string)

stack = []

for i in range(total_len):
    stack.append(input_string[i])
    if sub_len <= len(stack) and stack[-1] == sub_string[-1]:
        if stack[len(stack) - sub_len : len(stack)] == sub_string:
            for _ in range(sub_len):
                stack.pop()
if stack:
    print("".join(stack))
else:
    print("FRULA")

