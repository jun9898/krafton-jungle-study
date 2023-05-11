import math
A, B, V = map(int,input().split())

x = (V-B)/(A-B)
print(math.ceil(x))