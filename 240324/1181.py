# 조건을 잘못 읽었다. 해시를 쓸게 아니였음
#
# n = int(input())
# arr = list(set(input() for _ in range(n)))
#
# hash = [[] for _ in range(26)]
#
# for i in range(len(arr)):
#     hash[ord(arr[i][0]) - 97].append(arr[i])
#
# print(hash)
#
# for i in hash:
#     if i == None:
#         continue
#     print(i.sort())
import sys
input = sys.stdin.readline

n = int(input())
arr = list(set(input().strip() for _ in range(n)))

arr.sort()
arr.sort(key=len)

for i in arr:
    print(i)