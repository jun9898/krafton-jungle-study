import sys
input = sys.stdin.readline

n = int(input())

stack = []
result = 0

for i in range(n):
    x, y = map(int, input().split())
    # 스택이 있고 값이 작아진다면
    if stack and stack[-1] > y:
        while stack and stack[-1] > y:
            # 값이 변경될때마다 result를 더해줘야함
            tmp = stack.pop()
            if tmp != y:
                result += 1
        if not stack and y != 0:
            stack.append(y)
        elif stack and stack[-1] != y:
            stack.append(y)
    else:
        if y != 0:
            stack.append(y)

# 중복 제거
result += len(set(stack))
print(result)