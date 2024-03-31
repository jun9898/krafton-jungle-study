import sys
input = sys.stdin.readline


def search_m(animal_location, result):
    # 왼쪽, 오른쪽 유효 사거리 구하기
    left_effective_range = animal_location[0] + animal_location[1] - l
    right_effective_range = animal_location[0] - animal_location[1] + l
    # 사수가 배치되어있는 배열을 탐색할 기준
    left = 0
    right = len(m_list)-1
    # 모든 범위를 탐색할때까지
    while left <= right:
        mid = (left + right) // 2
        if left_effective_range <= m_list[mid] <= right_effective_range:
            result += 1
            break
        elif m_list[mid] < left_effective_range:
            left = mid + 1
        elif m_list[mid] > right_effective_range:
            right = mid - 1
    return result


# 사대의 수, 동물의 수, 사거리
m, n, l = map(int, input().split())
# 4수 리스트
m_list = list(map(int, input().split()))
m_list.sort()
# 동물 리스트
n_list = list()

result = 0

# 동물의 위치 좌표
for i in range(n):
    x,y = map(int, input().split())
    # 사수의 사정거리에 속한 동물만 arr에 추가
    if y <= l:
        n_list.append((x, y))

for i in n_list:
    result = search_m(i, result)

print(result)