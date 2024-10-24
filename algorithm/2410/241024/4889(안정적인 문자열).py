import sys
input = sys.stdin.readline

num = 0
while True:
    text = input().rstrip()
    if '-' in text:
        break
    stack = []
    for i in text:
        if not stack or i == "{":
            stack.append(i)
            continue
        if stack[-1] == "{":
            stack.pop()
        else:
            stack.append(i)

    num += 1
    result = 0
    if not stack:
        print(f'{num}. {result}' )
        continue
    tmp_stack = []
    for i in stack:
        if not tmp_stack and i == "}":
            tmp_stack.append("{")
            result += 1
        elif not tmp_stack and i == "{":
            tmp_stack.append("{")
        elif tmp_stack[-1] == "{" and i == "{":
            tmp_stack.pop()
            result += 1
        elif tmp_stack[-1] == "{" and i == "}":
            tmp_stack.pop()


    print(f'{num}. {result}' )




