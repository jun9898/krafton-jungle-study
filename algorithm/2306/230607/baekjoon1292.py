n, m = map(int, input().split())
array = [] 
i = 1
while True:
    array.extend([i]*i)
    i += 1
    if len(array) >= m:
        break
print(sum(array[n-1:m]))
