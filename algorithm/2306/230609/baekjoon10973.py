"""
메모리 초과
"""
# import sys
# input = sys.stdin.readline
# import itertools as it

# n = int(input())
# myArr = tuple(map(int, input().split()))
# arr = list(i for i in range(1,n+1))
# result = it.permutations(arr,n)
# result = list(result)
# for i in range(len(list(result))):
#     if result[i] == myArr:
#         if i == 0:
#             print(-1)
#             break
#         else:
#             for i in result[i-1]:
#                 print(i, end=" ")
#             break

N = int(input())
input_array = list(map(int, input().split()))

for i in range(N - 1, 0, -1):
    if input_array[i - 1] > input_array[i]:
        for j in range(N - 1, 0, -1):
            if input_array[i - 1] > input_array[j]:
                input_array[i - 1], input_array[j] = input_array[j], input_array[i - 1]
                input_array = input_array[:i] + sorted(input_array[i:],reverse=True)
                print(*input_array)
                exit()
print(-1)