# **********
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# **********
# star1 =["**********"]
# star2 = ["*        *"]
# for tower in range(2):
#     print(star1)
#     for tower2 in range(8):
#         print(star2)
#         if range == 8:
#             break

# print("1", end ="" )
# print("2", end ="")
# print("3")

# row = 0 #  행
# col = 0 #  열
# is_print = 0
# for row in range(10) :
#     col = 0
#     for col in range(10) :
#         is_print = 0
#         if ( row == 0 or row == 9 ):
#             is_print = 1
#         elif ( col == 0 or col == 9 ):
#             is_print = 1

#         if ( is_print == 1 ) :           
#             print("*", end ="")
#         else :
#             print(" ", end ="")
#     print("\r")        







# x = 0
# y = 0
# is_print = 0

# for y in range(10):
#     for x in range(10):
#         is_print = 0
#         if (x == 0 or x == 9):
#             is_print = 1
#         elif (y ==0 or y==9):
#             is_print = 1
        
#         if (is_print == 1) : 
#             print("*", end ="")
#         else:
#             print(" ", end = "")
#     print("\r")





























x = 0
y = 0
pain = 0

for y in range(10):
    pain = 0
    for x in range(10):
        pain = 0
        if ( x == 0 or x == 9):
            pain = 1
        elif ( y == 0 or y == 9 ):
            pain = 1
        
        if (pain == 1):
            print("*", end= "")
        else:
            print(" ", end= "")
    print("\r")
