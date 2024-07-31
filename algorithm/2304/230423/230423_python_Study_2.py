# 매개변수 앞에 * 기호를 붙혀주면 튜플로 만들어준다.
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

a = add_many(1,2,3,4,5,6,7,8,9,10)
print(a)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    
    return result

print(add_mul("mul", 1,2,3,4,5))
print(add_mul("add", 1,2,3,4,5))

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)

def say(name, age, man=True):
    print(f'my name is {name}')
    print(f'my age is {age}')
    if man:
        print("i'm a man")
    else:
        print("i'm a woman")

say("jeon", 26)