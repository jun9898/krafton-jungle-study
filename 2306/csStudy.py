# 선택정렬의 구현
array = [3,4,2,6,7,1,8,9]

for i in range(len(array)):
    for j in range(len(array)):
        if array[i] < array[j]:
            array[i], array[j] = array[j], array[i]

print(array)

# 재귀의 기본적인 모습
def star(n):
    if n == 0:
        return
    star(n-1)

    for i in range(n):
        print("*", end='')
    print()


n = int(input())
star(n)

