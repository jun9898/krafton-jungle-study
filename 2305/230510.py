N = int(input())
line = 0
endIndex = 0

while N > endIndex:
    line += 1 # while문이 N회 반복되며 사선으로 line을 그렸음을 의미
    endIndex += line # 해당 사선에 존재하는 수의 index의 수를 구한다 ex) 1 + 2 + 3 + 4....

top = 0
bottom = 0
gap = endIndex - N # 해당 라인의 최대 인덱스 - 입력값으로 내가 원하는 칸의 값을 구한다.
if line % 2 == 0:
    top = line - gap 
    bottom = gap + 1 
elif line % 2 != 0:
    top = gap + 1
    bottom = line - gap

print(f'{top}/{bottom}')



