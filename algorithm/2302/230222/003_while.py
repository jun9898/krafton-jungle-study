# cnt = 1
# while cnt <= 100:
#     if cnt%3 == 0 and cnt%5 == 0:
#         print ("fizzbuzz")
#     elif cnt%3 == 0:
#         print ("fizz")
#     elif cnt%5 == 0:
#         print ("buzz")
#     else:
#         print (cnt)
#     cnt = cnt + 1
    


n = int(input("input number:"))
for cnt in range(1,n+1): 
    num = str(cnt)
    count = 0
    for x in num:
        if (x=='3') or (x=='6') or (x=='9'):
            count += 1
    if count == 0:
        print(cnt, end=' ')
    else:
        print(count*'짝!', end=' ')

    
# n = int(input("input number:"))

# for game in range (1,1+n):
#     i = str(game)
#     count = 0
#     for x in i:
#         if (x == '3') or (x == '6') or (x == '9'):
#             count += 1
#     if count == 0:
#         print(game, end= ' ')
#     else:
#         print(count*'짝', end=' ')


    
i = 1
while i <= 100:
    j = str(i)
    count = 0
    for x in j:
        if x == '3' or x == '6' or x == '9':
            count += 1
    if count == 0:
        print(j, end= " ")
    else:
        print(count*'짝', end= " ")
    i += 1



# n = int(input("input number:"))

# for game in (1,1+n):
#     i = str(game)
#     count = 0
#     for x in i:
#         if (x == '3') or (x == '6') or (x == '9'):
#             count += 1
#     if count == 0:
#         print(game, end= ' ')
#     else:
#         print(count*'짝', end=' ')














