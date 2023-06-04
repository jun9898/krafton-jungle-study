# 집가서 주석달기
"""
deque 짱
"""
import sys
from collections import deque as de

input = sys.stdin.readline

n, k = map(int, input().split())
array = de(i for i in range(2, n+1))
result = []

while array:
    a = array[0]
    for _ in range(len(array)):
        if array[0] % a == 0:
            result.append(array.popleft())
        else:
            array.rotate(-1)

print(result[k-1])

