import sys
input = sys.stdin.readline

A, B, C, D = input().rstrip().split()
tmp1 = A + B
tmp2 = C + D

print(int(tmp1) + int(tmp2))
