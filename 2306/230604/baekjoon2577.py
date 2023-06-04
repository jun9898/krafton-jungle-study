# 쉬워서 해설 스킵!
import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

strN = str(A*B*C)

for i in range(10):
    strI = str(i)
    print(strN.count(strI))