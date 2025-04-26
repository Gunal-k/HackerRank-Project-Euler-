t = int(input())
for _ in range(t):
    n = int(input())
    sum_n = n * (n + 1) // 2
    sum_squares = n * (n + 1) * (2 * n + 1) // 6
    print(sum_n**2 - sum_squares)