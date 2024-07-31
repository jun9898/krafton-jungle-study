
fullPlate = list()
for i in range(8):
    plate = list(input())
    fullPlate.append(plate)

count = 0
for i in range(8):
    for j in range(0,8,2):
        if (i+1) % 2 == 0:
            if fullPlate[i][j+1] == "F":
                count += 1
        else:
            if fullPlate[i][j] == "F":
                count += 1

print(count)


