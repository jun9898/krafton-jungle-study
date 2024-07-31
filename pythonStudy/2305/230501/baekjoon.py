# A, B = input().split()
# print(int(A) + int(B))
# print(int(A) - int(B))
# print(int(A) * int(B))
# print(int(A) // int(B))
# print(int(A) % int(B))

# id = input()
# print(int(id) - 543)

# A, B, C = input().split()
# A = int(A)
# B = int(B)
# C = int(C)
# print((A+B)%C)
# print(((A%C) + (B%C))%C)
# print((A*B)%C)
# print(((A%C) * (B%C))%C)

# A = int(input())
# B = input()
# a = []
# for i in B:
#     a.append(i)
# for j in range(len(a)):
#     j += 1
#     print(A*int(a[-j]))
# print(A*int(''.join(a)))

# A, B, C = input().split()
# print(int(A) + int(B) + int(C))

# print("\    /\ ")
# print(" )  ( ')")
# print("(  /  )")
# print(" \(__)|")

# print("|\_/|")
# print("|q p|   /}")
# print('( 0 )"""\ ')
# print('|"^"`    |')
# print("||_/=\\\\__|")

# A, B = input().split()
# A = int(A)
# B = int(B)
# if A > B:
#     print(">")
# elif A < B:
#     print("<")
# elif A == B:
#     print("==")

# A = int(input())
# B = int(input())
# if A > 0  and B > 0: print("1")
# elif A < 0  and B > 0: print("2")
# elif A < 0  and B < 0: print("3")
# elif A > 0  and B < 0: print("4")

# H, M = map(int, input().split())
# bakingTime = int(input())
# cookingTime = M + bakingTime
# while True:
#     if cookingTime >= 60:
#         if H == 23:
#             H = 0
#             cookingTime -= 60
#         else:
#             H += 1
#             cookingTime -= 60
#     else:
#         break
# print(H, cookingTime)

# dice_1, dice_2, dice_3 = map(int, input().split())
# if dice_1 == dice_2 == dice_3: print(10000 + dice_1*1000)
# elif dice_1 == dice_2: print(1000 + dice_1*100)
# elif dice_1 == dice_3: print(1000 + dice_1*100)
# elif dice_3 == dice_2: print(1000 + dice_3*100)
# else: print(100 * max(dice_1, dice_2, dice_3))

# N = int(input())
# for i in range(1,10):
#     print(N, '*', i, '=', N*i)

# N = int(input())
# for i in range(N):
#     num1, num2 = map(int,input().split())
#     print(num1 + num2)

# N = int(input())
# result = 0
# for i in range(N+1):
#     result += i
# print(result)

# price = int(input())
# count = int(input())
# result = 0
# for i in range(count):
#     num1, num2 = map(int,input().split())
#     result += (num1 * num2)
# if price == result:
#     print('Yes')
# else:
#     print('No')
    
# num = int(input())
# for i in range(num):
#     result = num / 4
# print('long ' * int(result) + 'int' )

# import sys
# s= sys.stdin.readline().rstrip()
# s = int(s)
# x = 1
# for i in range(s):
#     num1, num2 = sys.stdin.readline().rstrip().split()
#     c = int(num1) + int(num2)
#     print("Case #" + str(x) + ":", num1, "+", num2, "=", c)
#     x += 1

# import sys
# star = sys.stdin.readline().rstrip()
# star = int(star)
# for i in range(1, star+1):
#     print(" "*(star-i) + "*"*i)

# import sys
# while True:
#     num1, num2 = map(int, sys.stdin.readline().rsplit())
#     print(num1 + num2)

# while True:
#     try:
#         A, B = map(int, input().split())
#         print(A+B)
#     except:
#         break

# n = int(input())
# nList = list(map(int, input().split()))
# x = int(input())
# print(nList.count(x))

# n = map(int, input())
# List = list(map(int, input().split()))
# print(min(List), max(List))

# List = []
# for i in range(1, 10):
#     x = int(input())
#     List.append(x)

# print(max(List))
# print(List.index(max(List))+1)

basketCount, count = map(int, input().split())
basket = [0] * basketCount
for i in range(count):
    x, y, z = map(int, input().split())
    for j in range(x-1, y):
        basket[j] = z
for i in range(basketCount):
    print(basket[i], end= ' ')