#Q1
Q1_test_list = [80,75,55]
Q1_test_append = 0
for i in Q1_test_list:
    Q1_test_append += i

print(Q1_test_append/len(Q1_test_list))

#Q2
num = 13
if (num%2==0):
    print("짝수")
else :
    print("홀수")


#Q3, Q4
number = "881120-1068234"
num_split = (number.split('-'))
a = num_split[1]
 
print(num_split[0])
print(num_split[1])
print(num_split[1][0])

#Q5
q5 = "a:b:c:d"
print(q5.replace(":", "#"))

#Q6
q5 = [1,3,5,4,2]
q5.sort()
q5.reverse()
print(q5)

#Q7
# q7_list = ['life', 'is', 'too', 'short']
# q7_list_append = ""
# for i in q7_list:
#     q7_list_append += i + " "
# print(q7_list_append)
# my result

q7_list = ['life', 'is', 'too', 'short']
q7_list_append = " ".join(q7_list)
print(q7_list_append)

#Q8
# q8_tuple = (1,2,3)
# q8_list = list(q8_tuple)
# q8_list.append(4)
# q8_tuple_append = tuple(q8_list)
# print(q8_tuple_append)
# my result

q8_tuple = (1,2,3)
q8_tuple_append = q8_tuple + (4, )
print(q8_tuple_append)

#Q10
a = {'a':90, 'b':80, 'c':70}
print(a.pop('b'))

#Q11 
a = [1,1,1,1,2,3,3,3,3,3,5,5,5,5,4]
a_set = set(a)
a_set_list = list(a_set)
print(a_set_list)


