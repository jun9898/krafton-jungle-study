import sys
input = sys.stdin.readline

n = int(input())
input_arr = list(map(int, input().split()))
stack = []
result = [0] * n

for index in range(n-1, -1, -1):
    temp = input_arr[index]
    if len(stack) == 0:
        stack.append([index,temp])
        continue
    elif temp <= stack[-1][1]:
        stack.append([index,temp])
        continue
    elif temp > stack[-1][1]:
        while len(stack) != 0 and stack[-1][1] < temp:
            pop_stack = stack.pop(-1)
            result[pop_stack[0]] = index+1
    stack.append([index,temp])
print(*result)




