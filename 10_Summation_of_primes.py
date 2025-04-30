import bisect

MAX_N = 10**6
is_prime = [True] * (MAX_N + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX_N**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX_N+1, i):
            is_prime[j] = False

primes = [i for i, val in enumerate(is_prime) if val]

prefix_sum = [0]
for p in primes:
    prefix_sum.append(prefix_sum[-1] + p)

def prefix_sum_of_primes(n):
    idx = bisect.bisect_right(primes, n)
    print(prefix_sum[idx])
    
t = int(input())

if 1<= t <= (10**4):
    for _ in range(t):
        prefix_sum_of_primes(int(input()))