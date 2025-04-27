def get_primes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    for number in range(2, limit + 1):
        if is_prime[number]:
            primes.append(number)
            for multiple in range(number*2, limit+1, number):
                is_prime[multiple] = False
    return primes

t = int(input().strip())
primes = get_primes(900000)
for a0 in range(t):
    n = int(input().strip())
    print(primes[n-1])