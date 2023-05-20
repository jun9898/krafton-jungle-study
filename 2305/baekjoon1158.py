import sys
input = sys.stdin.readline

# deque 말고 수열로 풀어봤음

n, k = input().split()
intn = int(n)
intk = int(k) -1
intktest = int(k) -1
listTest = [i for i in range(1, intn+1)]
result = []
print(listTest)

lenlist = len(listTest)


while True:
    if intk <= len(listTest):
        result.append(listTest.pop(intk))
        intk += intktest
    elif len(listTest) == 0:
        break
    elif intk > len(listTest):
        intk = intk % len(listTest)
        continue
        result.append(listTest.pop(intk))

print(str(result).replace("[", "<").replace("]", ">"))


# 1 2 3 4 5 6 7

