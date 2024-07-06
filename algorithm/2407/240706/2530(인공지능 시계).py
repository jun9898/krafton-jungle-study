import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

t = int(input())

s = (C + t) % 60
tmp_m = (C + t) // 60

m = (B + tmp_m) % 60
tmp_h = (B + tmp_m) // 60

h = (A + tmp_h) % 24

print (h, m, s)
