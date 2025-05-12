import math

def sum_fact(x):
    return sum(int(i) for i in str(x))

def fact(n):
    return sum_fact(math.factorial(n))

t = int(input())
for _ in range(t):
    n = int(input())
    print(fact(n))