def max_product_of_consecutive_digits(n, k, num_str):
    max_product = 0

    for i in range(n - k + 1):
        product = 1
        for j in range(k):
            digit = int(num_str[i + j])
            product *= digit
        max_product = max(max_product, product)

    return max_product

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    print(max_product_of_consecutive_digits(n,k,num))