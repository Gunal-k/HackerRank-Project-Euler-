MOD = 10**9 + 7
MAX = 1000

fact = [1] * (2 * MAX + 1)
inv_fact = [1] * (2 * MAX + 1)

for i in range(2, 2 * MAX + 1):
    fact[i] = fact[i - 1] * i % MOD

inv_fact[2 * MAX] = pow(fact[2 * MAX], MOD - 2, MOD)
for i in range(2 * MAX - 1, 0, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

def nCr(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

t = int(input())
if 1 <= t <= 1000:
    for _ in range(t):
        m, n = map(int, input().split())
        if 1 <= m <= 500 and 1 <= n <= 500:
            print(nCr(m + n, n))