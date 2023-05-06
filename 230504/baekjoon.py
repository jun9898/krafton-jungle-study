# croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# word = input()

# for i in croatia:
#     word = word.replace(i, "*")
# print(len(word))

# count = int(input())
# gWordList = []
# countGword = 0
# word = 0

# for i in range(count):
#     gWord = input()
#     gWordList.append(gWord)

# for i in gWordList:
#     gWordCount = []
#     error = 0
#     for j in i:
#         if j not in gWordCount:
#             gWordCount.append(j)
#         else:
#             j.count(gWordCount) > 0
#             error += 1
#     if error == 0:
#         word +=1

# print(word)   문제풀이 실패 해설보고 비교

# n = int(input())

# groupWord = 0
# for i in range(n):
#     word = input()
#     error = 0
#     for j in range(len(word)-1):
#         if word[j] != word[j+1]:
#             newWord = word[j+1:]
#             if newWord.count(word[j]) > 0:
#                 error += 1
#     if error == 0:
#         groupWord += 1

# N = int(input())
# result = []
# for _ in range(N):
#     str = input()
#     Flag = True
    
#     stack = []
#     for i in str:
#         if i not in stack or i == stack[-1]:
#             stack.append(i)
#         else:
#             Flag = False
        
#     result.append(Flag)
# print(result.count(True))
