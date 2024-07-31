# n = int(input("insert number : "))
# for i in range(1,1+n):
#     j = str(i)
#     v = 0
#     for x in j:
#         if x =='3' or x =='6' or x == '9':
#             v += 1
#     if v == 0:
#         print (j, end= " ")
#     else:
#         print ("짝!"*v, end= " ")
#     i += 1

# x = {"a":",", "b":"?"}

dic = {}
while ( True ):
    c = str(input("type char    : "))
    if ( c == "exit"):
        break
    t = str(input("type target  : "))
    dic[c] = t

n = str(input("type word        : "))
for i in n:
    for j in i:
        if j in dic:
            print(dic[j], end= "")
        else:
            print(i, end= "")
        
    # if i == "a":
    #     print(x["a"], end= "")
    # elif i == "b":
    #     print(x["b"], end= "")
    # else:
    #     print(i, end= "")
    # for y in i:
    #     print("y->",y)
        # if y == "a":
        #     print(x["a"], end= "")
        # elif y == "b":
        #     print(x["b"], end= "")
        # else:
        #     print(y, end= "")
    


