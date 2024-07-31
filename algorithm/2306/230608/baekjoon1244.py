import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int,input().split()))


m = int(input())

def commendM(num):
    for i in range(len(array)):
        if (i+1) % num == 0:
            if array[i] == 0:
                array[i] = 1
            else:
                array[i] = 0

def commendW(num):
    num -= 1
    if array[num] == 0:
        array[num] = 1
    else:
        array[num] = 0
    for i in range(1,len(array)//2):
        if i + num >= len(array) or num - i < 0:
            break
        if array[num-i] == array[num+i]:
            if array[num-i] == 0:
                array[num-i] = 1
                array[num+i] = 1
            else:
                array[num-i] = 0
                array[num+i] = 0
        else:
            break




for i in range(m):
    x, y = map(int,input().split())
    if x == 1:
        commendM(y)
    if x == 2:
        commendW(y)
    
for i in range(1,n+1):
    print(array[i-1], end = " ")
    if i % 20 == 0 :
        print()