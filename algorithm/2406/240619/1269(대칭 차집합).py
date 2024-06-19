import sys
input = sys.stdin.readline

n, m = map(int, input().split())
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))

lenA = len(setA-setB)
lenB = len(setB-setA)
print(lenA + lenB)
