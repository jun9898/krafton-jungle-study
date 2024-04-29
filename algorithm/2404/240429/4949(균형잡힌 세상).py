import sys
input = sys.stdin.readline

while True:
    input_string = input().rstrip()
    if input_string == ".":
        break
    stack = []
    flag = True
    for i in input_string:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")" or i == "]":
            if len(stack) == 0:
                flag = False
                break
            if i == ")":
                if stack[-1] == "(":
                    stack.pop()
                    continue
            elif i == "]":
                if stack[-1] == "[":
                    stack.pop()
                    continue
            flag = False
    if flag == True and len(stack) == 0:
        print("yes")
        continue
    print("no")

