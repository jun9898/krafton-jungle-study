# 2440 별찍기
# n = int(input())

# for i in range(n, 0, -1):
#     print("*"*i)

# 10870 피보나치
# n = int(input())
# if n == 0:
#     print(0)
#     quit()

# array = [0,1]

# for i in range(1, n):
#     num = array[i-1] + array[i]
#     array.append(num)

# print(array[-1])

#2441 별찍기
n = int(input())

for i in range(n, 0, -1):
    print(" "*(n-i),end="")
    print("*"*i)



