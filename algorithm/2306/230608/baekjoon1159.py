n = int(input())
namelist = dict()

for i in range(n):
    nameFirst = (input())[0]
    if nameFirst in  namelist:
        namelist[nameFirst] += 1
    else:
        namelist[nameFirst] = 1

result = []

for i in namelist:
    if namelist[i] >= 5:
        result.append(i)
if result:  
    result.sort()
    print("".join(result))
else:
    print("PREDAJA")