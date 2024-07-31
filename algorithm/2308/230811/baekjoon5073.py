listTest = []
for i in range(3):
    listTest.append(int(input()))
if sum(listTest) != 180:
    print("Error")
elif listTest[0] == listTest[1] == listTest[2]:
    print("Equilateral")
elif listTest[0] == listTest[1] or listTest[1] ==  listTest[2] or listTest[0] == listTest[2]:
    print("Isosceles")
elif listTest[0] != listTest[1] != listTest[2]:
    print("Scalene")
