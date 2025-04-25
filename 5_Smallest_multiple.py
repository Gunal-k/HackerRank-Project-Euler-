import math

def lcm(a,b):
    return abs(a*b)//math.gcd(a,b)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    res = 1
    for i in range(2,n+1):
        res = lcm(res,i)
    print(res)