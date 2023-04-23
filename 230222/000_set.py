# prime = {1,2,3,4,5,6,7,8,9,10}
# fib = {1,3,5,7,9,11,13}
# i = prime | fib
# print (i)

# dice = {1,2,3,4,5,6}
# even = {2,4,6,8}

# i = dice - even
# print (i)

dice = {1,2,3,4,5,6}
even = {1,2,3,5,7,9}

i = dice&even
ii = dice^even
print(ii)

# number_0 = [0,0,1,2,3,4,5,6]
# number_1 = set(number_0)

# print(len(number_0), len(number_1))

# prime = {2,3,5,7,13,17}
# fib = {1,1,2,3,5,8,13}
# prime_fib = prime & fib
# if 13 in prime_fib:
#     print ("13은 피보나치 수이고, 소수이기도 합니다.")
# if {2,3} <= prime_fib:
#     print ("2,3 은 피보나치 수이고,소수이기도 합니다.")


