from collections import deque

array = list(input())
string = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
stringUpper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

result = ''
for i in array:
    dequeArray = deque(string)
    dequeArrayUpper = deque(stringUpper)
    if i in dequeArray:
        while dequeArray[0] != i:
            dequeArray.rotate(-1)
        dequeArray.rotate(-13)
        result += dequeArray[0]
    elif i in dequeArrayUpper:
        while dequeArrayUpper[0] != i:
            dequeArrayUpper.rotate(-1)
        dequeArrayUpper.rotate(-13)
        result += dequeArrayUpper[0]
    else:
        result += i
print(result)