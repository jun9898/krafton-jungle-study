# Q1

# def is_odd(i):
#     if i%2==0: print("이 수는 짝수입니다")
#     else: print("이 수는 홀수입니다")

# is_odd(122)

# Q2

# def averageAll(*inputNum):
#     result = 0
#     for i in inputNum:
#         result += i
#     averageNum = result/len(inputNum)
#     print (averageNum)

# averageAll(12,13,16,123,15)

# Q3

# input1 = int(input("input your 1st num : "))
# input2 = int(input("input your 2nd num : "))

# total = input1 + input2
# print(f"두 수의 합은 {total} 입니다")

# Q4

# print("you", "need", "python")

# Q5

# f1 = open("test.txt", "w")
# f1.write("Life is too short")
# f1.close()

# f2 = open("test.txt", "r")
# print(f2.read())

# Q6

# inputString = (input("input String here : "))
# f1 = open("test1.txt", "a")
# f1.write(inputString)
# f1.write("\n")
# f1.close()

# f2 = open("test1.txt", "r")
# print(f2.read())
# f2.close

# Q7

f1 = open("test.txt", "r")
readText = f1.read()
print(readText)
f1.close


f2 = open("test.txt", "w")
readText = readText.replace("java", "python")
f2.write(readText)
print(readText)
f2.close

# rt = "java is run"
# rtReplace = rt.replace("java", "ppp")
# print(rtReplace)

# Q8 

# import sys

# result = 0
# args = sys.argv[1:]
# for i in args:
#     result += int(i)
    
# print(result)