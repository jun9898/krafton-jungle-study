import sys
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    tmp = input().split()
    if tmp[0] == "1":
        stack.append(int(tmp[1]))
    elif tmp[0] == "2":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif tmp[0] == "3":
        print(len(stack))
    elif tmp[0] == "4":
        if stack:
            print(0)
        else:
            print(1)
    elif tmp[0] == "5":
        if stack:
            print(stack[-1])
        else:
            print(-1)
