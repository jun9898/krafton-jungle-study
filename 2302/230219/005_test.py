#
# ***********
#      *
#      *
#      *
#      *
#      *
#      *
#      *
#      *
# ***********

# row ?
# col ?


x = 0
y = 0
p = 0

for y in range(10):
    p = 0
    for x in range(11):
        p = 0
        if ( x == 5):
            p = 1
        elif ( y == 0 or y == 9):
            p = 1
        
        if (p == 1):
            print("*", end= "")
        else:
            print(" ", end= "")
    print("\r")

        