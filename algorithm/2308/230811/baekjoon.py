listTest = list(map(int,input().split()))
answerList = []

if listTest[0] < (listTest[2] - listTest[0]):
    answerList.append(listTest[0])
else:
    answerList.append((listTest[2] - listTest[0]))

if listTest[1] < (listTest[3] - listTest[1]):
    answerList.append(listTest[1])
else:
    answerList.append((listTest[3] - listTest[1]))

print(min(answerList))


