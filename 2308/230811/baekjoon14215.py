listTest = sorted(map(int, input().split()))
result = listTest[0] + listTest[1] + min(listTest[2], listTest[0]+listTest[1]-1)
print(result)
