MAX = 5 * (10**6)
collatz_cache = [0] * MAX
collatz_cache[1] = 1

# Precompute Collatz sequence lengths
for i in range(2, MAX):
    n = i
    steps = 0
    while n >= MAX or collatz_cache[n] == 0:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
        if n < MAX and collatz_cache[n] != 0:
            steps += collatz_cache[n]
            break
    collatz_cache[i] = steps

# Precompute the number with the longest Collatz sequence for each number
max_length = [0] * MAX
max_num = 1
for i in range(1, MAX):
    if collatz_cache[i] >= collatz_cache[max_num]:
        max_num = i
    max_length[i] = max_num

# Process queries
t = int(input())
if 1 <= t <= 10**4:
    results = []
    for _ in range(t):
        n = int(input())
        results.append(max_length[n])
    print("\n".join(map(str, results)))