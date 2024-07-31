# """
# 알파벳 순서대로 정렬이 안되서 실패
# """
# import sys
# from collections import deque
# import copy

# input = sys.stdin.readline

# arr = deque(input().rstrip())

# answer = []
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         arrFirst = []
#         arrSecond = deque()
#         arr[i],arr[j] = arr[j],arr[i]
#         arrCopy = copy.deepcopy(arr)
#         while arrCopy:
#             if arrCopy[0] == arrCopy[-1]:
#                 arrFirst.append(arrCopy.popleft())
#                 arrSecond.appendleft(arrCopy.pop())
#                 if len(arrCopy) == 1:
#                     result = []
#                     lastword = arrCopy.pop()
#                     result.extend(arrFirst)
#                     result.extend(lastword)
#                     result.extend(arrSecond)
#                     answer.append(result)
#                     break
#                 elif not arrCopy:
#                     result = []
#                     result.extend(arrFirst)
#                     result.extend(arrSecond)
#                     answer.append(result)
#                     break
#             else:
#                 break
# else:
#     if not answer:
#         print("I'm Sorry Hansoo")
#         quit()

# answerQustion = ['~']
# for i in answer:
#     for j in range(len(i)//2):
#         if ord(i[j]) < ord(answerQustion[j]):
#             answerQustion = i
# print("".join(answerQustion))


import sys
from collections import deque
from collections import Counter

input = sys.stdin.readline

arr = list(input().rstrip())

arr.sort()
count = Counter(arr)

odd = 0
lastword = ''

for i in count:
    if count[i] % 2 != 0:
        odd += 1
        if odd > 1:
            print("I'm Sorry Hansoo")
            quit()



arrFirst = deque()
arrSecond = deque()

for _ in range(len(arr)+1):
    if len(arr) != 0 and arr.count(arr[0]) % 2 == 0:
        arrFirst.append(arr.pop(0))
        arrSecond.appendleft(arr.pop(0))
    elif len(arr) == 0:
        break
    elif arr.count(arr[0]) % 2 != 0:
        if arr.count(arr[0]) // 2 > 0:
            arrFirst.append(arr.pop(0))
            arrSecond.appendleft(arr.pop(0))
        else:
            lastword = (arr.pop(0))

result = []
result.extend(arrFirst)
try:
    if lastword:
        result.extend(lastword)
except:
    pass
result.extend(arrSecond)

print("".join(result))

    
















