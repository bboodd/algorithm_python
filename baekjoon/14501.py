n = int(input())
a = []
for _ in range(n):
    a.append(list(map,int(input().split())))

t_cost = 0
for i in range(len(a)):
    cost = a[i][1]
    day = a[i][0]
    for j in a[i:]:
        while day < n+1:
            