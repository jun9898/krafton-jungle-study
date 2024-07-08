import sys
input = sys.stdin.readline

A = int(input())

op = input().rstrip()

B = int(input())

if op == '+':
    print(A + B)
else:
    print(A * B)