stringArray = []
while True:
    string = input()
    if string == "0":
        break
    stringArray.append(string)

for i in stringArray:
    revers = i[::-1]
    if i == revers:
        print("yes")
    else:
        print("no")
    