def even_fib_sum(n):
    a, b = 1, 2
    total = 0
    while b <= n:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    return total
    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(even_fib_sum(n))