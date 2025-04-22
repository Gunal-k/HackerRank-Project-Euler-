def sum_divisible_by(k, n):
    p = (n - 1) // k
    return k * p * (p + 1) // 2

t = int(input())
for _ in range(t):
    n = int(input())
    result = sum_divisible_by(3, n) + sum_divisible_by(5, n) - sum_divisible_by(15, n)
    print(result)