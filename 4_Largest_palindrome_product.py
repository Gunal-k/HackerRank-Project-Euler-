palindromes = []
for i in range(100, 1000):
    for j in range(i, 1000):
        product = i * j
        if str(product) == str(product)[::-1]:
            palindromes.append(product)
            
palindromes.sort()

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    i = 0
    while True:
        if palindromes[i] < n:
            i+=1
        else:
            i-=1
            break
    print(palindromes[i])