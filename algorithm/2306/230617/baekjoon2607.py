import sys
input = sys.stdin.readline

n = int(input())

firstWord = list(input().rstrip())

arr = []

result = 0
for _ in range(n-1):
    word = input().rstrip()
    wordF = firstWord[:]
    count = 0
    for w in word:
        if w in wordF:
            wordF.remove(w)
        else:
            count += 1
    if count < 2 and len(wordF) < 2:
        result += 1
print(result)


        
            