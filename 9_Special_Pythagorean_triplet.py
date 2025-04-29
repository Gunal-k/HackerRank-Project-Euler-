def max_pythagorean_triplet_product(n):
    max_product = -1
    for a in range(1, n // 3):
        b = (n * (n - 2 * a)) // (2 * (n - a))
        c = n - a - b
        if a * a + b * b == c * c:
            max_product = max(max_product, a * b * c)
    return max_product
    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(max_pythagorean_triplet_product(n))