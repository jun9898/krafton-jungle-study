string = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
stringUpper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number = ['1','2','3','4','5','6','7','8','9','0']

while True:
    upperCount = 0
    lowerCount = 0
    numCount = 0
    spaceCount = 0

    try:
        array = list(input())
        for i in array:
            if i in stringUpper:
                upperCount += 1
            elif i in string:
                lowerCount += 1
            elif i in number:
                numCount += 1
            else:
                spaceCount += 1
    except:
        break
    print(lowerCount, upperCount, numCount, spaceCount)

"""
isupper = True
islower = True
isdigit = True
를 사용하면 리스트를 정의하지 않아도 풀 수 있다.
"""