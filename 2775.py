a=[[i for i in range(1,15)]for _ in range(15)]

for i in range(1,15):
    for j in range(14):
        a[i][j] = 0
        for k in range(j+1):
            a[i][j] += a[i-1][k] 
n = int(input())

for _ in range(n):
    x = int(input())
    y = int(input())
    print(a[x][y-1])