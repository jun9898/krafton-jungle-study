# import time as t
# a = t.asctime(t.localtime(t.time()))
# print(a)
# a = t.ctime()
# print(a)

# basketCount, count = map(int, input().split())
# basket = [i+1 for i in range(basketCount)]

# for i in range(count):
#     x, y = map(int, input().split())
#     returnX = basket[x-1]
#     basket[x-1] = basket[y-1]
#     basket[y-1] = returnX

# print(*basket)

# num = []
# for i in range(10):
#     a = int(input())
#     num.append(a % 42)
# num = set(num)
# print(len(num))

# basketCount, count = map(int, input().split())
# basket = [i+1 for i in range(basketCount)]

# for i in range(count):
#     x, y = map(int, input().split())
#     basketReverse = basket[x-1 : y]
#     basketReverse.reverse()
#     basket[x-1 : y] = basketReverse
    
# print(*basket)


# basketCount, count = map(int, input().split())
# basket = [i+1 for i in range(basketCount)]

# for i in range(count):
#     x, y = map(int, input().split()) 
#     basketReverse = basket[x-1 : y]
#     basketReverse.reverse()
#     basket[x-1 : y] = basketReverse

# print(*basket)

# M = int(input())
# testList = list(map(int, input().split()))
# maxScore = max(testList)

# result = 0
# for i in testList:
#     result += (i/maxScore)*100
# print(result/M)
    
# num = int(input())
# for i in range(num):
#     strTest = str(input())
#     print(strTest[0] + strTest[-1])

# print(ord(str(input())))

# num = int(input())
# string = str(input())
# a = 0
# if len(string) != num:
#     quit
# for i in string:
#     a += int(i)

# print(a)

# S = str(input())
# alphabet = list(range(97,123))
# for i in alphabet:
#     print(S.find(chr(i)), end= ' ')

# M = int(input())
# for i in range(M):
#     count, string = map(str, input().split())
#     for i in string:
#         count = int(count)
#         print(i*count, end='')
#     print()

# S = str(input())
# S = S.split()
# print(len(S))

# string1, string2 = map(str, input().split())
# string1 = int(string1[::-1])
# string2 = int(string2[::-1])
# if string1 > string2:
#     print(string1)
# else:
#     print(string2)

# alpabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
# word = input()

# time = 0
# for i in alpabet_list:
#     print(i)
#     for j in i:
#         print(j)
#         for x in word:
#             if i == x:
#                 time += alpabet_list.index(i) +3
# print(time)

# alpabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
# word = input()

# time = 0
# for i in alpabet_list:
#     for j in i:
#         for x in word:
#             if j == x:
#                 time += alpabet_list.index(i) +3
                
# print(time)


while True: print(input())
a = "python"
print(a)


