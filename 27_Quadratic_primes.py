import math

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return set(i for i, val in enumerate(is_prime) if val)

def count_primes(a, b, prime_set):
    n = 0
    while True:
        value = n * n + a * n + b
        if value < 2 or value not in prime_set:
            break
        n += 1
    return n

def solve_euler027(N):
    max_limit_a = 1000
    max_value = max_limit_a ** 2 + max_limit_a * N + N
    prime_set = sieve(max_value)

    max_count = 0
    best_a, best_b = 0, 0

    for a in range(-max_limit_a, max_limit_a + 1):
        for b in range(-N, N + 1):
            if abs(b) not in prime_set:
                continue
            count = count_primes(a, b, prime_set)
            if count > max_count or (count == max_count and a * b < best_a * best_b):
                max_count = count
                best_a, best_b = a, b

    return best_a, best_b

if __name__ == "__main__":
    N = int(input())
    a, b = solve_euler027(N)
    print(f"{a} {b}")