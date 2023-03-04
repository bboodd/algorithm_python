m = int(input())
n = int(input())
a = []
for i in range(1,101):
    if m <= i**2 <= n:
        a.append(i**2)
        
if len(a) == 0:
    print(-1)
else:
    print(sum(a))
    print(a[0])