import time

'''
이 코드는 이중 for문으로 구성된 함수의 실행 시간을 측정하여
입력 크기 n에 따른 실행 시간 증가를 확인합니다.
'''

def example_function(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += i * j
    return total

def measure_time(func, n):
    start_time = time.time()
    func(n)
    end_time = time.time()
    return end_time - start_time

for n in [100, 200, 400, 800]:
    elapsed_time = measure_time(example_function, n)
    print(f"n={n}, time={elapsed_time:.6f} seconds")
