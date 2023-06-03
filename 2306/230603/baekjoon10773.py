# 너무 간단한 스택문제이다 따로 해설은 하지 않겠다.
import sys
input = sys.stdin.readline

n = int(input())

stack = []

for i in range(n):
    n = int(input())
    if n == 0:
        stack.pop()
        continue
    stack.append(n)

print(sum(stack))

