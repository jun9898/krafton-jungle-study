# a, b = map(int,input().split())

# print(b*2-a)

# from datetime import datetime

# print((datetime.today().strftime("%Y-%m-%d")))


# n = int(input())

# for i in range(1,n+1):
#     print("*"*i)
# for i in range(n-1,0,-1):
#     print("*"*i)

# for i in range(3):
#     array = list(map(int, input().split()))
#     if array.count(0) == 1:
#         print("A")
#     if array.count(0) == 2:
#         print("B")
#     if array.count(0) == 3:
#         print("C")
#     if array.count(0) == 4:
#         print("D")
#     if array.count(0) == 0:
#         print("E")

# a, b = map(int,input().split())
# if a > 0 and b > 0:
#     print(max(a,b)-min(a,b))
# else:
#     print(abs(a) + abs(b))

# array = list(map(int, input().split()))
# array.sort()
# print(*array)

# import sys
# input = sys.stdin.readline

# T = int(input())

# for _ in range(T):
#     a, b = map(int, input().split())
#     a = a % 10
    
#     if a == 0:
#         print(10)
#     elif a == 1 or a == 5 or a == 6:
#         print(a)
#     elif a == 4 or a == 9:
#         b = b % 2
#         if b == 1:
#             print(a)
#         else:
#             print((a * a) % 10)
#     else:
#         b = b % 4
#         if b == 0:
#             print((a**4) % 10 % 10 % 10)
#         else:
#             print((a**b) % 10 % 10 % 10)

array = []

for i in range(5):
    array.append(int(input()))

print(int(sum(array)/len(array)))
array.sort()
print(array[len(array)//2])