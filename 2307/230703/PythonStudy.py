class Cal:
    # 여기서 self는 해당 클래스로 생성된 객체의 값을 뜻하므로
    # 따로 인수를 전달해주지 않아도 된다.
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result


    
cal1 = Cal()

cal1.setdata(4,3)
print(cal1.add())