import sys
input = sys.stdin.readline

tmp = input().rstrip()

stack = []

for i in tmp:
    if 65 <= ord(i) <= 90:
        print(i, end='')
    else:
        if i == "(":
            stack.append(i)
        elif i == ")":
            while stack and stack[-1] != "(":
                print(stack.pop(), end="")
            stack.pop()
        elif i == "*" or i == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                print(stack.pop(), end='')
            stack.append(i)
        elif i == "+" or i == "-":
            while stack and stack[-1] != '(':
                print(stack.pop(), end='')
            stack.append(i)
while stack:
    print(stack.pop(), end="")