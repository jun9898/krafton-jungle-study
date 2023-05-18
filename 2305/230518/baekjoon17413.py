import sys
from collections import deque
input = sys.stdin.readline

# s = str(input())
# string = ""

# for i in s:
#     if "<" in i:
#         string += i
#         print(i)
#     for j in i.split("<"):
#         print(j)
#         string += "<" + j + ">"

# print(string)



# string = ""

# for i in s:
#     if i[0] == "<":
#         string += i
#     else:
#         sortI = i[::-1]
#         string += sortI + " "

# print(string)

# s = list(map(str, input().split()))
# string = ""

# for i in s:
#     if "<" in i:
#         indexFirst = i.index("<")
#         indexSecond = i.index(">")
# #     string += i[::-1]
# # print(string)
# print(indexFirst, indexSecond)

word = input().replace('\n', '')

Stack = ""
result = ""
flag = False


for i in word:
    if flag == False:
        if "<" == i:
            flag = True
            Stack = Stack + i
        elif i == " ":
            Stack = Stack + i
            result += Stack
            Stack = ""

        else:
            Stack = i + Stack
    
    elif flag == True:
        Stack = Stack + i
        if i == ">":
            result += Stack
            flag = False
            Stack = ""
print(result + Stack)







