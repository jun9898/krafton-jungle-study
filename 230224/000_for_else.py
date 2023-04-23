
a_num = 2

for num in range(2,a_num):
    if a_num%num == 0:
        print(a_num, " 은 소수가 아닙니다." )
        break
else:
    print(a_num, "은 소수.")




def fizzbuzz(count = 12,  fizz = 3, buzz = 5):
    for cnt in range(1, count + 1):
        if cnt%fizz==0 and cnt%buzz==0:
            print("fizzbuzz", end= " ")
        elif cnt%fizz == 0:
            print("fizz", end= " ")
        elif cnt%buzz == 0:
            print("buzz", end= " ")
        else:
            print(cnt, end= " ")

fizzbuzz(20,4,5)
        
# 
# 
# dic = {}
# def change(n,m):
    # while True:    
        # i = input("cha     : ")
        # if i == "exit":
            # break
        # j = input("tar     : ")
        # dic[i] = j
# 
# change(1,2)
# print(dic)