# 매직직넘버버
magicArray = set(range(1, 10001))
removeArray = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    removeArray.add(i)

for i in sorted(magicArray - removeArray):
    print(i)