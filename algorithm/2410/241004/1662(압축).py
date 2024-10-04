import sys
from collections import deque

input = sys.stdin.readline

# 3 3(56 2(7 1(9)))
# 3 3(56 2(79))
# 3 3(56 7979)
# 3 567979567979567979
# print(len("3567979567979567979")) = 19

# 이 과정 반복 - 메모리 초과
# stack 3 3 ( 5 6 2 ( 7 1 ( 9 )   event 발생 ( 가 나올때까지 tmp에 문자열 저장 후 pop
# stack 3 3 ( 5 6 2 ( 7 1   tmp = "9" * stack.pop()
# stack 3 3 ( 5 6 2 ( 7 9   stack.extent(tmp)

# arr 3 3   length = 2 tmp = "3" stack = []
# arr 3 3 (   length = 0 tmp = "3" stack = [("3", 1)]
# arr 3 3 ( 5 6 2   length = 3 tmp = "2" stack = [("3", 1)]
# arr 3 3 ( 5 6 2 (  length = 0 tmp = "2" stack = [("3", 1), ("2", 2)]


arr = deque(input().rstrip())
stack = []

length = 0
tmp = ""
while arr:
    cur = arr.popleft()
    if cur.isdigit():
        length += 1
        tmp = cur
    elif cur == "(":
        stack.append((tmp, length - 1))
        length = 0
    else:
        mul, pre = stack.pop()
        length = (int(mul) * length) + pre

print(length)
