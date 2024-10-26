import sys
from collections import defaultdict, deque
input = sys.stdin.readline

s, p = map(int, input().split())

dna_string = input().rstrip()

required_A, required_C, required_G, required_T = map(int, input().split())

current_count = defaultdict(int)

slide = deque(dna_string[:p])

for i in slide:
    current_count[i] += 1

def is_valid():
    return (current_count['A'] >= required_A and
            current_count['C'] >= required_C and
            current_count['G'] >= required_G and
            current_count['T'] >= required_T)

result = 0
if is_valid():
    result += 1

for i in range(p, s):
    outgoing_char = slide.popleft()
    current_count[outgoing_char] -= 1

    incoming_char = dna_string[i]
    slide.append(incoming_char)
    current_count[incoming_char] += 1

    if is_valid():
        result += 1

print(result)
