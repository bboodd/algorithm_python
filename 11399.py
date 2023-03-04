n = int(input())
p = list(map(int,input().split()))

p.sort()
first = p[0]
for i in range(1,len(p)):
    p[i] = first+p[i]
    first = p[i]
print(sum(p))