MAX_LIMIT = 28123

divisor_sums = [0] * (MAX_LIMIT + 1)
for i in range(1, MAX_LIMIT + 1):
    for j in range(2 * i, MAX_LIMIT + 1, i):
        divisor_sums[j] += i

abundant_numbers = set()
for i in range(1, MAX_LIMIT + 1):
    if divisor_sums[i] > i:
        abundant_numbers.add(i)

can_be_expressed = [False] * (MAX_LIMIT + 1)
for a in abundant_numbers:
    for b in abundant_numbers:
        s = a + b
        if s <= MAX_LIMIT:
            can_be_expressed[s] = True
        else:
            break

t = int(input())
for _ in range(t):
    n = int(input())
    if n > MAX_LIMIT:
        print("YES")
    else:
        print("YES" if can_be_expressed[n] else "NO")