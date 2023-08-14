n = int(input())

answerArr = []

for i in range(n):
    value = 0
    for j in str(i):
        value += int(j)
    if (i+value) == n:
        answerArr.append(i)

if answerArr:
    print(min(answerArr))
else:
    print(0)