# x, y = input().split()
# print(int(x, int(y)))

# N, B = list(map(int,input().split()))
# tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# answer = ''
# while N!= 0:
#     answer += str(tmp[N % B])
#     N = N//B

# print(answer[::-1])

# class Cal:
#     def __init__(self):
#         self.value = 0

#     def add(self, val):
#         self.value += val

#     def minus(self, val):
#         self.value -= val

# cal = Cal()
# cal.add(200)
# cal.minus(3)
# print(cal.value)

# class MaxCal(Cal):
#     def add(self, val):
#         self.value += val
#         if self.value > 100:
#             self.value = 100

# cal = MaxCal()
# cal.add(200)
# print(cal.value)

a = list(filter(lambda x:x>0, [1,-3,5,2]))
print(a)

print(int('0xea', 16))

print(list(map(lambda x: x*3, [1,2,3,4])))

listNum = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(listNum) + min(listNum))

print(round(17/3, 4))