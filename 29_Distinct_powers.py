n=int(input())
dump=set()
count=0
for x in range(2, n+1):
    if x not in dump:
        res=set()
        y=2
        while x**y <=n:
            dump.add(x**y)
            for m in range(2*y, y*(n+1), y):
                if m>n:
                    res.add(m)
            y+=1
        count+=len(res)+n-1
print(count)