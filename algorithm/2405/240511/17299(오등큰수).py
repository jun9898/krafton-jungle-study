import sys
input = sys.stdin.readline

n = int(input())
stack = list(map(int, input().split()))
largest_stack = []
res = []

dic = dict()

for i in stack:
    if i not in dic:
        dic[i] = 1
        continue
    dic[i] += 1

while stack:
    cur = stack.pop()
    if len(largest_stack) == 0:
        largest_stack.append(cur)
        res.append(-1)
    elif dic[largest_stack[-1]] > dic[cur]:
        res.append(largest_stack[-1])
        largest_stack.append(cur)
    elif dic[cur] >= dic[largest_stack[-1]]:
        while len(largest_stack) != 0 and dic[cur] >= dic[largest_stack[-1]]:
            largest_stack.pop()
        if len(largest_stack) == 0:
            res.append(-1)
        else:
            res.append(largest_stack[-1])
        largest_stack.append(cur)

for i in range(n-1, -1, -1):
    print(res[i], end=" ")


