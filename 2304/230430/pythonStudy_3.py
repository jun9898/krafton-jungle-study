print("what a wonderful world!")
for i in range(5):
    print('have fun python')

# print('input score')
# dan = int (input())
# print('=================')

# for i in range(1, 10):
#     result = dan * i
#     print(result)

# print('=================')


# import random

# val = random.randint(1, 11)
# while True:
#     yourNumber = (int(input('guess random number : ')))
#     if val == yourNumber:
#         print(f" your right! random number is {val}")
#         break
#     elif yourNumber > val:
#         print("down")
#         continue
#     elif yourNumber < val:
#         print("up")
#         continue

# num = 2
# n = int(input(' dan : '))
# n1 = int(input(' except : '))
# for i in range(2, n+1 ):
#     if i % n1 == 0:
#         continue
#     for j in range(1,10):
#         print(i, '*', j, '=', i*j)


# sum = 0
# i = 0
# n = int(input(' n : '))
# while i <= n:
#     if i%2 == 0 or i%7 == 0:
#         sum = sum+i
#     i += 1

# print(sum)


# for i in range(n+1):
#     if i % 2 == 0 or i % 7 == 0:
#         sum = sum + i
# print(sum)

# result = 0
# a = 0
# b = 0
# while a >= b:

#     a = int(input(' a : '))
#     b = int(input(' b : '))

# for i in range(a, b+1):
#     if i % 2 == 0 and i % 3 == 0:
#         continue
#     elif i % 2 == 0:
#         result += i
# print(result)

# a = 1
# b = 30
# n = 0
# while n>30 or n<1:
#     n = int(input("n : "))

# print (n)

# i = 1
# while a >= 1:
#     n2 = (a+b)//2
#     print(i, '번째 step', 'n2 : ', n2)
#     if n2 == n:
#         print("성공", i, "번만에 맞았다") 
#         break
#     elif n>n2:
#         a=n2+1 #16
#         b=b #30
#     elif n<n2:
#         a=a #1
#         b=n2-1 #14
#     i += 1


# while True:
#     dan = int(input("input dan : "))
#     if dan < 1 or dan > 9:
#         print('input num 1 ~ 9')
#         continue
#     break
# count = 1
# while True:
#     print(count, '단')
#     count2 = 1
#     while True:
#         print(count, '*', count2, '=', count*count2, end=" ")
#         count2 += 1
#         if count2>9:
#             break
#     count += 1
#     print()
#     if count>dan:
#         break

# sum = 0
# i = 0
# while i <= 100:
#     i += 1
#     if i % 3 == 0 and i % 5 == 0:
#         print(i, end=',')
#         sum += i
# print()
# print('sum = ', sum)    

# import turtle as t
# t.shape('turtle')
# a = ['red', 'orange', 'yellow', 'violet', 'lightsalmon', 'green', 'blue' ]
# for i in range(len(a)):
#     t.color(a[i])
#     t.forward(100)
#     t.right(360/len(a))

from turtle import *
shape('turtle')
pensize(5)
colormode(255)
goto(0,0)

col = 255
col_t = 0
for i in range(19,-1,-1):
    color(col_t,0,col)
    begin_fill()
    for j in range(i):
        forward(100)
        right(360/i)
    end_fill()
    col = col-int(255/19)
    col_t=col_t+int(255/19)