import sys
input = sys.stdin.readline

n = int(input())
setArray = set()

for i in range(n):
    commend = input().split()
    if "add" in commend:
        x = int(commend[-1])
        setArray.add(x)
    if "remove" in commend:
        x = int(commend[-1])
        setArray.discard(x)
    if "check" in commend:
        x = int(commend[-1])
        if x in setArray:
            print(1)
        else:
            print(0)
    if "toggle" in commend:
        x = int(commend[-1])
        if x in setArray:
            setArray.discard(x)
        else:
            setArray.add(x)
    if "all" in commend:
        setArray = set(i for i in range(1,21))
    if "empty" in commend:
        setArray = set()


    
    
    
