import re
from collections import deque
import sys

input = sys.stdin.readline

T = int(input())
for i in range(T):
    stack1 = deque()
    flag = True
    error_flag = False
    commend = list(input().rstrip())
    arr_length = int(input())
    stack1.extend(list(map(int, re.findall(r'\d+', input().rstrip()))))
    for j in commend:
        if j == "R":
            flag = not flag
        elif j == "D":
            if len(stack1) == 0:
                error_flag = True
                break
            if flag:
                stack1.popleft()
            elif not flag:
                stack1.pop()
    if error_flag:
        print("error")
        continue
    if flag:
        print("[" + ",".join(map(str, stack1)) + "]")
    elif not flag:
        stack1.reverse()
        print("[" + ",".join(map(str, stack1)) + "]")


