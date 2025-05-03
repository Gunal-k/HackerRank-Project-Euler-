total = 0

for line in range(int(input())):
    n = list(map(int, input().split()))
    total += sum(n)

print(str(total)[:10])