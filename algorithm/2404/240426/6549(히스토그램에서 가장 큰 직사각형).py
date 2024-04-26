import sys
input = sys.stdin.readline

while True:

    n = list(map(int, input().split()))
    if n[0] == 0:
        break
    max_res = 0
    stack = []

    for i, h in enumerate(n):
        if i == 0:
            continue
        if stack and stack[-1][1] > h:
            while stack:
                stack_i, stack_h = stack.pop()
                cur_index = 1
                if stack:
                    cur_index = stack[-1][0] + 1
                result = (i - cur_index) * stack_h
                max_res = max(max_res, result)
                if not stack or stack[-1][1] <= h:
                    break
        if not stack or stack[-1][1] <= h:
            stack.append((i, h))

    while stack:
        stack_i, stack_h = stack.pop()
        cur_index = 1
        if stack:
            cur_index = stack[-1][0] + 1
        result = (n[0]+1 - cur_index) * stack_h
        max_res = max(max_res, result)

    print(max_res)

