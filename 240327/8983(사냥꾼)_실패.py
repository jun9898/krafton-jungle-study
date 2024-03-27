import sys
input = sys.stdin.readline


# 탐색 시작
# 사수의 위치, 사거리, 탐색 시작점(Y좌표), tmp
def binary_search(x, l):
    global tmp
    if len(n_list) == 0:
        return
    if l <= 0:
        return
    search_left(x-l)
    search_right(x+l)
    binary_search(x, l-1)  # 재귀 호출된 결과를 tmp에 할당
    return


def search_left(location):
    global tmp
    animals_found = [i for i in n_list if i[0] == location]
    for animal in animals_found:
        print(animal)
        n_list.remove(animal)
        tmp += 1

def search_right(location):
    global tmp
    animals_found = [i for i in n_list if i[1] == location]
    for animal in animals_found:
        print(animal)
        n_list.remove(animal)
        tmp += 1


# 사대의 수, 동물의 수, 사거리
m, n, l = map(int, input().split())
m_list = list(map(int, input().split()))
m_list.sort()
n_list = list()

# 동물의 위치 좌표
for i in range(n):
    x,y = map(int, input().split())
    # 사수의 사정거리에 속한 동물만 arr에 추가
    if y <= l:
        # 왼쪽 대각, 오른쪽 대각
        n_list.append((x-y, x+y))

result = 0

# 사대의 위치를 순회
for i in m_list:
    tmp = 0
    binary_search(i, l)
    result += tmp

print(result)



