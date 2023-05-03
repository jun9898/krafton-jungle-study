# print("""         ,r'"7
# r`-_   ,'  ,/
#  \. ". L_r'
#    `~\/
#       |
#       |
#       """)

# x = list(map(int, input().split()))

# x[0] = 1 - x[0]
# x[1] = 1 - x[1]
# x[2] = 2 - x[2]
# x[3] = 2 - x[3]
# x[4] = 2 - x[4]
# x[5] = 8 - x[5]
# print(*x)

# star = int(input())
# for i in range(1,star+1):
#     print(" "*(star-i)+"*"*(2*i-1)) 
# for i in range(star-1,0,-1):
#     print(" "*(star-i)+"*"*(2*i-1))

# basketCount, count = map(int, input().split())
# basket = [i+1 for i in range(basketCount)]
# # print(basket)

# for i in range(count):
#     x, y, z = map(int, input().split()) 
#     x, y, z = x-1, y-1, z-1
#     basket = basket[:x] + basket[z:y+1] + basket[x: z] + basket[y+1:]
#     # print(basket)

# print(*basket)

# String = list(str(input()))
# newString = list(String)
# String.reverse()
# if String == newString:
#     print("1")
# else:
#     print("0")

# words = input().upper()
# uniqueWords = list(set(words))

# countList = []
# for i in uniqueWords:
#     count = words.count(i)
#     countList.append(count)

# if countList.count(max(countList)) > 1:
#     print("?")
# else:
#     maxIndex = countList.index(max(countList))
#     print(uniqueWords[maxIndex])

testCase = int(input())

for i in range(testCase):
    score = list(map(int,input().split()))
    averageScore = sum(score[1:])/score[0]
    count = 0
    for j in score[1:]:
        if averageScore < j:
            count +=1
    rate = count/score[0] * 100
    print(f'{rate:.3f}%')


