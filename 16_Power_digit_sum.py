def pow_of_digit(n):
    val = 2**n
    total = 0
    if (len(str(val)) > 0):
        while val !=0:
            total += val % 10
            val//=10
    else:
        total = val
    return total
        

t = int(input())
for _ in range(t):
    n = int(input())
    print(pow_of_digit(n))