n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

m = 0

for i in range(n):
    m+=a[i]*b[i]
    
print(m)