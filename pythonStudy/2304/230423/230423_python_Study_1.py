import random

# a = [1,2,3,4]
# result = [num * 3 for num in a]
# print(result)

# a = [1,2,3,4]
# result = [num%2  for num in a]
# print(result)

# a = [1,2,3,4,5,6,7,8]
# result = [i * 3 for i in range(50)]
# print(result)

# result = [x * y for x in range(2,10)
#                 for y in range(1,10)]
# print(result)

# result = [x * y for x in range(2,10)
#                 for y in range(1,10)]

# a = random.randint(1,10)
# b = random.randint(1,50)
# val = random.randint(a,b)
# if a>b:
#     temp = a
#     a = b
#     temp = a
# print(a)

# for i in range(1,6,1):
#     print(i)

# for i in range(1,6):
#     print('*'*i)

# for i in range(4):
#     print('*'*5)

# for i in range(5):
#     print('*'*(5-i))

# for i in range(2,10):
#     for j in range(1,10):
#         print(i, "*", j, "=", i*j)
#     print()

# a = 1
# def vartest(a):
#     a = a + 1
#     return a

# a = vartest(a)

# print(a)

# add = lambda a, b: a+b
# result = add(3,4)
# print(result)

# number = int(input("숫자를 입력하세요 : "))
# print(number)

# print("life", "is", "too short")
# print(a)

# f = open("새파일2.txt", "w")
# for i in range(1, 13):
#     data = f"{i} 번째 줄입니다. \n"
#     f.write(data)
# f.close()


# f = open("새파일2.txt", "r")
# line = f.readline()
# print(line)
# f.close()

# f = open("새파일2.txt", "r")
# while True:
#     line = f.readline()
#     if not line:break
#     print(line, end="")
# f.close()

# f = open("새파일2.txt", "r")
# while True:
#     data = input()
#     if not data :break
#     print(data)
# f.close()


# f = open("새파일2.txt", "r")
# lines = f.readlines()
# for line in lines:
#     line = line.strip()
#     print(line)
# f.close()


# f = open("새파일2.txt", "r")
# data = f.read()
# print(data)
# f.close()

# f = open("새파일2.txt", "r")
# for line in f:
#     print(line)
# f.close

# f = open("새파일.txt", "a")
# for i in range(10, 20):
#     data = f"{i} 번째 줄입니다. \n"
#     f.write(data)
# f.close

# f = open("foo.txt", "w")
# f.write("life is too short, you need python")
# f.close

with open("foo.txt", "w") as f:
    f.write("life is too short, you need more money")