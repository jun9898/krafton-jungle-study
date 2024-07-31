n = input()
arr = input().split()

count = 0
for i in arr:
    if i[0] == n:
        count += 1

print(count)