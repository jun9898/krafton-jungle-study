import sys
from collections import deque
input = sys.stdin.readline().strip()

# 단순 리스트와 문자열을 이용해서 문제를 푸려고 노력했으나 코드가 너무 길어질게 뻔해 stack을 응용해봤다.
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

# 입력값을 개행문자 '\n'을 제외해서 입력받는다.
word = input

# stack과 stack 내부에서 문자열을 뒤집어 result에 넣을것이다.
Stack = ""
result = ""
# flag는 마치 스위치와 같다. 특정 조건을 달성하면 True로 변환하여 True 상태의 조건문을 실행할것이다.
flag = False


# 입력받은 word의 글자를 하나하나 i에 대입 해 루프를 돌린다.
for i in word:
    # 만약 flag가 False라면 아래 조건문을 실행한다.
    if flag == False:
        # 만약 "<" 기호가 i라면
        if "<" == i:
            # 문자열을 뒤집지 않은상태로 stack에 넣기 위해 스위치를 킨다
            flag = True
            # stack에 < 를 입력
            Stack = Stack + i
        # 만약 i 가 공백이라면
        elif i == " ":
            # 공백을 기준으로 문자열을 끊어주니 stack에 공백을 추가해준 뒤 result에 더해주고 stack 내부를 비워준다.
            Stack = Stack + i
            result += Stack
            Stack = ""

        else:
            # 위 2가지 조건에 해당되지 않는 경우 그냥 stack에 역순으로 i를 추가한다.
            Stack = i + Stack
    
    # 위 조건문의 수행으로 flag가 True로 바뀐 상태라면
    elif flag == True:
        # stack에 순서대로 i 값을 대입하여 문자열을 뒤집지 않는다.
        Stack = Stack + i
        # 만약 i가 >라면 
        if i == ">":
            # result에 그동안 stack에 쌓인 문자열을 더해준다.
            result += Stack
            # 괄호가 닫혔으므로 문자열 스위치를 다시 내린다.
            flag = False
            # stack에 있는 모든 내용은 result에 추가 되었으므로 stack을 비워준다.
            Stack = ""
            # 다시 루프 시작


# 혹시라도 < > 태그 뒤에 문자열이 올 수도 있으니 마지막에 stack 안의 내용을 추가해준다.
print(result + Stack)







