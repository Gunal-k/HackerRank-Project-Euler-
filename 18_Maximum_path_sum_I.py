def triangle_sum(triangle):
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]


for _ in range(int(input())):
    a = []
    for i in range(int(input())):
        row = list(map(int,input().split()))
        a.append(row)
    
    print(triangle_sum(a))