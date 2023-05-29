
def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1 / n2

def rem(n1,n2):
    return n1 % n2

def sha(n1,n2):
    return n1 // n2

def squ(n1,n2):
    return n1 ** n2

while True:
    print('-'*60)
    select = int(input("1. +, 2. -, 3. *, 4. /, 5. %. 6. //, 7. **, 8. end : " ))
    if select == 8:
        print("break")
        break
    i = float(input("input your 1st number : "))
    j = float(input("input your 2nd number : "))

    if select == 1:
        print(f'{i} + {j} =  {add(i,j)}')

    if select == 2:
        print(f'{i} - {j} =  {sub(i,j)}')

    if select == 3:
        print(f'{i} * {j} =  {mul(i,j)}')

    if select == 4:
        print(f'{i} / {j} =  {div(i,j)}')

    if select == 5:
        print(f'{i} % {j} =  {rem(i,j)}')

    if select == 6:
        print(f'{i} // {j} =  {sha(i,j)}')

    if select == 7:
        print(f'{i} ** {j} =  {squ(i,j)}')













