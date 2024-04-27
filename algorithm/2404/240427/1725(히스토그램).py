import sys
input = sys.stdin.readline


n = int(input())
stack = []
his = []
for i in range(n):
    his.append(int(input()))
max_res = 0
for i in range(n):
    cur_index = i
    while stack and stack[-1][1] > his[i]:
        cur_index, stack_h = stack.pop()
        result = (i - cur_index) * stack_h
        max_res = max(max_res, result)
    stack.append([cur_index, his[i]])


while stack:
    cur_index, stack_h = stack.pop()
    result = (n - cur_index) * stack_h
    max_res = max(max_res, result)

print(max_res)

