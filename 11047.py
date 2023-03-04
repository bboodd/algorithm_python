n,k = map(int,input().split())
count = 0
a = []
for i in range(n):
    a.append(int(input()))

while k > 0:
    if a[n-1] <= k:
        count += k // a[n-1]
        k %= a[n-1]
    n-=1
        
print(count)