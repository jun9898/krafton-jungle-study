from sys import stdin
from collections import defaultdict

def solve_test_case():
    text = stdin.readline().rstrip()
    n = int(stdin.readline())

    char_freq = {}
    for char in text:
        char_freq[char] = char_freq.get(char, 0) + 1

    positions = defaultdict(list)
    for i, char in enumerate(text):
        if char_freq[char] >= n:
            positions[char].append(i)

    if not positions:
        return -1, -1

    result_min = float('inf')
    result_max = 0

    for char_positions in positions.values():
        if len(char_positions) >= n:
            lengths = [end - start + 1
                       for start, end in zip(char_positions, char_positions[n-1:])]

            if lengths:
                result_min = min(result_min, min(lengths))
                result_max = max(result_max, max(lengths))

    return result_min, result_max

def main():
    T = int(stdin.readline())

    for _ in range(T):
        min_len, max_len = solve_test_case()
        if min_len == -1:
            print(-1)
        else:
            print(min_len, max_len)

if __name__ == "__main__":
    main()
