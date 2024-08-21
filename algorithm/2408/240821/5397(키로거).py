import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    tmp = list(input().rstrip())
    stack1 = deque()
    stack2 = deque()
    for i in tmp:
        if i != "<" and i != ">" and i != "-":
            stack1.append(i)
        elif stack1 and i == "<":
            stack2.appendleft(stack1.pop())
        elif stack2 and i == ">":
            stack1.append(stack2.popleft())
        elif stack1 and i == "-":
            stack1.pop()
    result = stack1 + stack2
    print("".join(result))



