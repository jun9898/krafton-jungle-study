import sys
input = sys.stdin.readline

n = int(input())
answerlist = []


i = 2

while i <= n:
    if n%i == 0:
        answerlist.append(i)
        n /= i

    else:
        i += 1

for i in answerlist:
    print(i)
        

