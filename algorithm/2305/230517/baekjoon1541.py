# 몸이 넘 안좋아 내일 마저 풀어보자.
firstCal = list(map(str, input().split('-')))
print(firstCal)
add = []
sub = []
count = 0

for i in firstCal:
    if '+' in i:
        sub = sum(list(map(int, i.split('+'))))
        
    else:
        add.append(int(i))
print(add() - sub())



