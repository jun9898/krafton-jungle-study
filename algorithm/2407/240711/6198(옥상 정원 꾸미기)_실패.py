import sys
input = sys.stdin.readline

N = int(input())
stack = []
result_stack = []

for i in range(N):
    tmp = int(input())
    if stack:
        key = list(stack[-1].keys())[0]
        if key < tmp:
            while stack and list(stack[-1].keys())[0] < tmp:
                cur = stack.pop()
                print(cur)
                pre = list(stack[-1].keys())[0]
    else:
        stack.append({tmp : 0})
    print(stack)


