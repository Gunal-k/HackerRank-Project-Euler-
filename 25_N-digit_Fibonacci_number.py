import math

def fibonacci_index_with_digits(d):
    if d == 1:
        return 1

    phi = (1 + math.sqrt(5)) / 2
    return math.ceil((d - 1 + math.log10(math.sqrt(5))) / math.log10(phi))

t = int(input())
for _ in range(t):
    a = int(input())
    print(fibonacci_index_with_digits(a))