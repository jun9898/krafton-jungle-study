import sys
input = sys.stdin.readline


def install_routers(houses, C, min_distance):
    routers_installed = 1
    last_router_position = houses[0]

    for i in range(1, len(houses)):
        if houses[i] - last_router_position >= min_distance:
            routers_installed += 1
            last_router_position = houses[i]

            if routers_installed == C:
                break

    return routers_installed == C


def find_max_distance(houses, C):
    houses.sort()
    start = 1
    end = houses[-1] - houses[0]
    result = 0

    while start <= end:
        mid = (start + end) // 2
        if install_routers(houses, C, mid):
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result


N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]

answer = find_max_distance(houses, C)
print(answer)
