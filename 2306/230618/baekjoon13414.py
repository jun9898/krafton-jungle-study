"""
시간 초과
"""
# import sys
# input = sys.stdin.readline

# n, m = map(int,input().split())

# queue = [] 
# for i in range(m):
#     stu = input().rstrip()
#     if stu in queue:
#         queue.append(queue.pop(queue.index(stu)))
#     else:
#         queue.append(stu)

# for i in range(n):
#     print(queue[i])

import sys
input = sys.stdin.readline

n, m = map(int,input().split())

dic = {}

for i in range(m):
    dic[input().rstrip()] = i

result = sorted(dic.items(), key= lambda x:x[1])

if (n > len(result)):
    n = len(result)

for i in range(n):
    print(result[i][0])
