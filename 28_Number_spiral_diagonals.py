MOD = 10**9 + 7

def modinv(a, mod):
    return pow(a, mod - 2, mod)

def diagonal_sum(n):
    if n == 1:
        return 1
    
    L = (n - 1) // 2

    inv6 = modinv(6, MOD)

    sum_k2 = (L * (L + 1) % MOD) * (2 * L + 1) % MOD
    sum_k2 = sum_k2 * inv6 % MOD
    term1 = (16 * sum_k2) % MOD

    sum_k = (L * (L + 1) // 2) % MOD
    term2 = (4 * sum_k) % MOD

    term3 = (4 * L) % MOD

    total = (1 + term1 + term2 + term3) % MOD
    return total

import sys
input = sys.stdin.read

data = input().split()
t = int(data[0])
cases = list(map(int, data[1:]))

for n in cases:
    print(diagonal_sum(n))