import sys
input = sys.stdin.readline

n = int(input())
stack = list(map(int, input().split()))
largest_stack = []
res = []

while stack:
    cur = stack.pop()
    if len(largest_stack) == 0:
        largest_stack.append(cur)
        res.append(-1)
    elif largest_stack[-1] > cur:
        res.append(largest_stack[-1])
        largest_stack.append(cur)
    elif cur >= largest_stack[-1]:
        while len(largest_stack) != 0 and cur >= largest_stack[-1]:
            largest_stack.pop()
        if len(largest_stack) == 0:
            res.append(-1)
        else:
            res.append(largest_stack[-1])
        largest_stack.append(cur)

for i in range(n-1, -1, -1):
    print(res[i], end=" ")


