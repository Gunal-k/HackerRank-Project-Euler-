def sum_of_proper_divisors(n):
    if n < 2:
        return 0
    divisors = {1}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            if i != n // i:
                divisors.add(n // i)
    return sum(divisors)

def find_amicable_numbers(limit):
    amicable_numbers = set()
    for a in range(2, limit):
        b = sum_of_proper_divisors(a)
        if b >= limit or b == a:
            continue
        if sum_of_proper_divisors(b) == a:
            amicable_numbers.add(a)
            amicable_numbers.add(b)
    return amicable_numbers
    
limit = 10**5
amicable_numbers = find_amicable_numbers(limit)

t = int(input())
for _ in range(t):
    val = int(input())
    print(sum(i for i in amicable_numbers if i <= val))