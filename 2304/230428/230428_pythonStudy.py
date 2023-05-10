from mod1 import *

class Fourcal:

    # __init__ 는 class를 사용하여 객체를 생성할때 초기값을 설정해준다.
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        resultAdd = self.first + self.second 
        return resultAdd
    
    def sub(self):
        resultsub = self.first - self.second 
        return resultsub

    def mul(self):
        resultmul = self.first * self.second 
        return resultmul

    def div(self):
        resultdiv = self.first / self.second 
        return resultdiv

# class 상속
class MoreFourCal(Fourcal):
    def pow(self):
        result = self.first ** self.second
        return result

# 메소드 오버라이딩
class SafeFourCal(Fourcal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4,0)
print(a.div())

print(add(1,7))

try:
    a = [1,2]
    print(a[1])
    print(4/10)
except (ZeroDivisionError, IndexError) as e :
    print(e)
else:
    print("오류 없음")

# try:
#     age = int(input('나이를 입력하세요.'))
# except:
#     print("입력이 정확하지 않습니다.")
# else:
#     if age <= 18:
#         print("미성년자 출입 금지입니다.")
#     else:
#         print("환영합니다")


class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("very fast")
eagle = Eagle()
eagle.fly()