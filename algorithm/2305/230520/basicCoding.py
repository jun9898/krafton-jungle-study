# 정렬 문제
# n = list(map(int, input().split()))

# def bubbleSort(arr):
#     listN = arr
#     n = len(arr)

#     for i in range(n):
#         for j in range(n):
#             if listN[i] > listN[j]:
#                 # temp = n[i]
#                 # 동시 스위칭이 되는구나
#                 listN[i], listN[j] = listN[j], listN[i]
#                 # n[j] = temp
#     return(listN)

# print(n)
        
# print(bubbleSort(n))


# 팩토리얼 함수

# def fac(n):
#     if n <= 1:
#         return 1
#     else:
#         return n*fac(n-1)

# n = int(input("n : "))
# print(fac(n))
# 재귀 함수의 개념과 작동 원리를 이해했지만 응용하려면 더 깊게 이해할 필요가 있을것같다.

# 피보나치 함수
import sys
input = sys.stdin.readline

def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n-2)+fibo(n-1)
        

n = int(input())
print(fibo(n))