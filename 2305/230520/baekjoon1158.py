import sys
input = sys.stdin.readline

# deque 말고 수열로 풀어봤음

n, k = map(int,input().split())
intn = int(n)
intk = int(k) -1
intktest = intk
listTest = [i for i in range(1, intn+1)]
result = []

while listTest:
    result.append(listTest.pop(intk))
    intk += intktest
    while listTest:
        if (intk >= len(listTest)):
            intk = intk % len(listTest)
        else:
            break

print(str(result).replace("[", "<").replace("]", ">"))


# 1 2 3 4 5 6 7

