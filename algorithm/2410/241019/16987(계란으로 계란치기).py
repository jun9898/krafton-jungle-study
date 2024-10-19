import sys
input = sys.stdin.readline

def get_broken_count(eggs):
    count = 0
    for egg in eggs:
        if egg[0] <= 0:
            count += 1
    return count


def break_eggs(current, eggs):
    global max_broken_eggs
    if current == n:
        max_broken_eggs = max(max_broken_eggs, get_broken_count(eggs))
        return

    if eggs[current][0] <= 0:
        break_eggs(current + 1, eggs)
    else:
        found_target = False
        for target in range(n):
            if current != target and eggs[target][0] > 0:
                found_target = True
                eggs[current][0] -= eggs[target][1]
                eggs[target][0] -= eggs[current][1]
                break_eggs(current + 1, eggs)
                eggs[current][0] += eggs[target][1]
                eggs[target][0] += eggs[current][1]
        if not found_target:
            break_eggs(n, eggs)


n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
max_broken_eggs = 0
break_eggs(0, eggs)
print(max_broken_eggs)
