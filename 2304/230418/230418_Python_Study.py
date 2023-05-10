# print("Hello World!")

# a = "Life is too short"
# print(len(a))

# y = 3.123456
# print(f'{y:10.4f}') 

# a = "python is the best choice"
# print(a.find('o'))

# a = "Life is too short"
# print(a.split())
# b = "a:b:c:d"
# print(b.split(':'))

# a = [1,2,3, [4,5,6]]
# print(a[1])
# print(a[0])
# print(a[-1])
# print(a[3])
# print(a[3][0])

# a = [1,2,3,4,5]
# print(a[0:2])

# print(a[:2])
# print(a[2:])

# a = [1,2,3]
# b = [4,5,6]
# print(a+b)

a = [1,2,3]
print(a*3)

a = [1,2,3]
a[2] = 4
print(a)

a = [1,2,3]
del a[2]
print(a)

a = [1,2,3]
a.append(4)
print(a)

a = [2,4,1,3]
a.sort()
print(a)

a = [1,2,3,4]
a.reverse()
print(a)


a = [1,2,3,4]
print(a.index(3))

a = [1,2,3,4]
a.insert(0, 4)
print(a)

a = [1,2,3,4]
a.remove(3)
print(a)

# fltmxm dyth RMwlqdjsorl

a = [1,2,3,4]
print(a.pop())
print(a)
4
[1,2,3]
# pop은 리스트의 마지막 요소를 리턴하고 그 요소는 삭제한다.

a = [1,2,3,4]
print(a.pop(2))
print(a)
3
[1,2,4]
# pop(x)는 x번째 요소를 리턴하고 그 요소는 삭제한다.

# 리스트 포함된 요소의 개수 세기

a = [1,2,3,1]
print(a.count(1))
2

# 리스트 확장

a = [1,2,3]
a.extend([4,5])
print(a)
[1,2,3,4,5]