import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n != -1:
        array = []
        for i in range(1,n):
            if n % i == 0:
                array.append(i)

        if sum(array) == n:
            for i in range(len(array)):
                array[i] = str(array[i])
            print(n,"="," + ".join(array))
        else:
            print(n, "is NOT perfect.")
    else:
        break