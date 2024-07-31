# Q1
# shirt

# Q2
i = 0
j = 0
while i <= 1000:
    if i % 3 == 0:
        j += i
    i += 1
print(j)

# Q3
i = 0
while i < 5:
    i += 1
    print("*" * i)
    
# Q4
i = 0
i_list = []
for i in range(100):
    i += 1
    i_list.append(i)

print(i_list)

# Q5

j = 0 
marks = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
for i in marks:
    j += i
print(j/len(marks))

# Q6

numbers = [1,2,3,4,5]
result = []
# for n in numbers:
#     if n % 2 == 1:
#         result.append(n*2)
# print(result)

result = [a * 2 for a in numbers if a % 2 == 1]
print(result)

