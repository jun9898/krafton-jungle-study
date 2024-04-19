import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    n = input()
    stack = []
    flag = True
    for j in n:
        if j == "(":
            stack.append(j)
        if j == ")":
            if len(stack) == 0:
                flag = False
                break
            if stack.pop() != "(":
                flag = False
                break
    if len(stack) != 0:
        flag = False
    if flag:
        print("YES")
    else:
        print("NO")
