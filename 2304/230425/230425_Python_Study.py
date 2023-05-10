# result = 0

# def add(num):
#     global result
#     result += num
#     return result

# print(add(3))
# print(add(5)) # result를 글로벌 함수로 지정해 config 값을 가진다.

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sum(self, num):
        self.result -= num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(5))
print(cal1.sum(4))