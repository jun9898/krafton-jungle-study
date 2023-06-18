
# string = ['a','e','i','o','u']

# while True:
#     n = input().rstrip()
#     flag = False
#     if n == 'end':
#         break
#     n = list(i for i in n)
#     for i in n:
#         if i in string:
#             flag = True
#             break
#     n = "".join(n)
#     if flag == True:
#         count = 0
#         for i in range(1,len(n)):
#             if n[i] == n[i-1]:
#                 if n[i] and n[i-1] == 'e':
#                     continue
#                 if n[i] and n[i-1] == 'o':
#                     continue
#                 count += 1
#         if count < 1:
#             print(f'<{n}> is acceptable.')
#         else:
#             print(f'<{n}> is not acceptable.')
#     else:
#         print(f'<{n}> is not acceptable.')

string = "aeiou"

while True:
    n = input()
    if n == "end":
        break
    countG = 0
    countG_C = 0
    countC_C = 0
    temp = ''

    flag = True

    for i in n:
        if i in string:
            countC_C = 0
            countG += 1
            countG_C += 1
            if countG_C >= 3:
                flag = False
            if temp == i:
                if i =='e' or i =='o':
                    pass
                else:
                    flag = False
        else:
            countG_C = 0
            countC_C += 1
            if countC_C >= 3:
                flag = False
            if temp == i:
                flag = False
        temp = i
    if countG < 1:
        flag = False
    
    if flag:
        print(f'<{n}> is acceptable.')
    else:
        print(f'<{n}> is not acceptable.')



 