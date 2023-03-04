n = int(input())
hight = []
weight = []
c = []
for i in range(n):
    h , w = map(int,input().split())
    hight.append(h)
    weight.append(w)

for x in range(n):
    rank = 1
    for y in range(n):
        if weight[x] < weight[y]:
            if hight[x] < hight[y]:
                rank += 1
    c.append(rank)
    
for m in c:
    print(m,end=' ')
print()

                
            