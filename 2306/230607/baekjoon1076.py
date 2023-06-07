color = ['black', 'brown', 'red', 'orange', 'yellow','green','blue','violet','grey','white']
number = ['0','1','2','3','4','5','6','7','8','9']
zeroCount = ['','0','00','000','0000','00000','000000','0000000','00000000','000000000']

inputColor = input()
inputColor2 = input()
inputColor3 = input()
result = ''

firstnum = color.index(inputColor)
result += number[firstnum]
secondnum = color.index(inputColor2)
result += number[secondnum]
thirdnum = color.index(inputColor3)
result += zeroCount[thirdnum]

print(int(result))