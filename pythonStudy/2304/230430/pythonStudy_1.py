class Bird:
    def fly(self):
        raise NotImplementedError


class Eagle(Bird):
    def fly(self):
        print("very Fast")


eagle = Eagle()
eagle.fly()

class MyError(Exception):
    def __str__(self):
        return "not good for nick name" 
    pass

def say_nick(nick):
    if nick == "test2":
        raise MyError()
    print(nick)

try:
    say_nick("test1")
    say_nick("test2")
except MyError as e:
    print(e)