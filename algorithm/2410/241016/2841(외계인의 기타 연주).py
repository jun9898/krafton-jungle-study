import sys
from collections import defaultdict

input = sys.stdin.readline

n, p = map(int, input().split())

stack_dict = defaultdict(list)

result = 0

for i in range(n):
    n , p = map(int, input().split())
    cur_stack = stack_dict[n]
    if not cur_stack:
        stack_dict[n].append(p)
        result += 1
    else:
        while cur_stack and p < cur_stack[-1]:
            cur_stack.pop()
            result += 1
        if not cur_stack or p > cur_stack[-1]:
            cur_stack.append(p)
            result += 1

print(result)
