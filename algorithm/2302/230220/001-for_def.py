
# for cnt in range(5):
#     cnt += cnt + 1
#     print(cnt)

# saving = 100
# for i in range(10):
#     saving += saving*0.05
# print(saving) #print 앞에 공백이 없으면 루프에 포함되지 않아 최종 값만 도출되지만 print 앞에 공백이 있다면 루프에 포함되어 출력을 반복한다

# i = [1,2,3,4,5,6]
# for ruf in i:  
#     if (ruf == 1 ):
#         print(1)

# the_list = [1,2,3,4,5,6]
# summ = 0

# for item in the_list:
#     summ = (summ + item)
# print(summ)

# abs(-2000) # abs는 수치의 절대값을 빼주는 함수이다

# int("100") #int("100",2) 이런식으로 표기하면 100을 2진수로 반환받을 수 있다.

# def destiny_tank():
#     tank = ["전차1","전차2","전차3","전차4","전차5","전차6"]
#     num = input("좋아하는 숫자를 입력하세요:")
#     idx = int(num) % len(tank)
#     print("당신의 운명의 전차는")
#     print(tank[idx]) 

# destiny_tank()
#함수를 정의하여 반복되는 작업을 단축할 수 있다

# def home():
#     room = ["pc", "mouse", "pen", "keybored"]
#     num = input("아무 숫자나 입력하세요.")
#     res = int(num) % len(room)
#     print("당신의 운명의 물건은")
#     print(room[res])

# home()
    
# def home(num):
#     room = ["computer", "pen", "mouse", "keybored"]
#     res = int(num) % len(room)
#     print ( "당신의 운명의 물건은")
#     print (room[res])

# num_str = input("좋아하는 숫자를 입력하세요")
# num = int(num_str)
# home(num)

# from random import randint
# num = randint(0,10)
# home(num)

# 함수와 난수 생성기를 이용한 코드

# def home(num):
#     room = ["a", "b", "c", "d", "e", "f"]
#     res = num % len(room)
#     return room[res]

# from random import randint
# num = randint(0,10)
# ran = home(num)
# print ( "오늘 당신의 행운의 물건은", ran, "입니다.")

# 리턴값을 이용하여 바깥 함수의 수식에 값을 대입할 수 있다.

# def cal_var(a_list):
#     total = sum(a_list)
#     length = len(a_list)
#     men = total/len(a_list)
#     val = 0

#     for height in a_list:
#         val += ( height - men )**2
#     val = val/len(a_list)

#     return val

# i = [158,157,163,157,145]
# ii= [143,167,170,165]
# iii= [127,172,140,160,174]

# i_var = cal_var(i)
# ii_var = cal_var(ii)
# iii_var = cal_var(iii)

# print(i_var**0.5)
# print(ii_var**0.5)
# print(iii_var**0.5)

# def 함수를 이용하여 복잡한 표준편차를 구하는 수식을 구현하였다

# def hi(num):
#     for hello in range(num):
#         print("안녕하십니까")

# hi(10)