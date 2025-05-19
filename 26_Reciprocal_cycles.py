def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def multiplicative_order(a, n):
    if gcd(a, n) != 1:
        return 0
    order = 1
    value = a % n
    while value != 1:
        value = (value * a) % n
        order += 1
    return order

def precompute_max_d(limit=10001):
    result_map = [0] * limit
    max_len = 0
    best_d = 0
    for d in range(2, limit):
        if gcd(d, 10) == 1:
            cycle_len = multiplicative_order(10, d)
            if cycle_len > max_len:
                max_len = cycle_len
                best_d = d
        result_map[d] = best_d
    return result_map

result_map = precompute_max_d()

t = int(input())
for _ in range(t):
    n = int(input())
    print(result_map[n - 1])