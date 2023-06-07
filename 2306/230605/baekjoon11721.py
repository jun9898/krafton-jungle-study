string = input()
stringArray = []

for i in string:
    stringArray.append(i)

n = 0
for i in range(len(stringArray)//10 + 1):
    print("".join(stringArray[n:n+10]))
    n += 10