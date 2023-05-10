# 별찍기
# **********
# *--------*
# *--------*
# *--------*
# *--------*
# *--------*
# *--------*
# **********
x=0
y=0

for y in range(1, 9):
    for x in range(1, 11):
        if (y == 1 or y == 8):
            print("*", end="")
        elif (x == 1 or x == 10):
            print("*", end="")
        else:
            print("-", end="")
        x += 1
    y += 1
    print()

test = 1
for number in range(10):
    if number % 2 == 0 : test += 1 
print (test)


result = [("*" if y == 1 or y == 8 or x == 1 or x == 10 else "-")
          for y in range(1, 9)
          for x in range(1, 11)]
          
# 출력
for i in range(0, len(result), 10):
    print("".join(result[i:i+10]))