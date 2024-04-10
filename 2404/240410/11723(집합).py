import sys
input = sys.stdin.readline


def add(S, x):
    x = int(x)
    S |= (1 << x) # 1을 X만클 shift 연산 한 뒤 or연산 실행
    return S


def remove(S, x):
    x = int(x)
    S &= ~(1 << x) # 1을 X만클 shift 연산 한 뒤 NAND연산 실행
    return S


def check(S, x):
    x = int(x)
    if S & (1 << x): #
        return True
    return False


def toggle(S, x):
    x = int(x)
    S ^= 1 << x
    return S


def all():
    S = (1 << 21) - 1
    return S


def empty():
    return 0



n = int(input())
S = 0

for i in range(n):
    commend = list(input().split())
    if commend[0] == "add":
        S = add(S, commend[1])

    elif commend[0] == "remove":
        S = remove(S, commend[1])

    elif commend[0] == "check":
        if check(S, commend[1]):
            print(1)
            continue
        print(0)

    elif commend[0] == "toggle":
        S = toggle(S, commend[1])

    elif commend[0] == "all":
        S = all()

    elif commend[0] == "empty":
        S = empty()
