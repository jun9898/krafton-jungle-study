import sys
input = sys.stdin.readline

score = []
for i in range(10):
    score.append(int(input()))

result = 0
for i in range(10):
    result += score[i]
    if result == 100:
        print(result)
        quit()
    elif result > 100:
        minScore = result - score[i]
        minScore = abs(100-minScore)
        maxScore = abs(100-result)
        if minScore > maxScore:
            print(result)
            quit()
        elif minScore < maxScore:
            print(result - score[i])
            quit()
        else:
            print(result)
            quit()
print(result)

