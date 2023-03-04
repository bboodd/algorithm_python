a,b = list(input().split())

a = int(a[2])*100+int(a[1])*10+int(a[0])
b = int(b[2])*100+int(b[1])*10+int(b[0])

if a>b :
    print(a)
else:
    print(b)
    
    
a,b = input().split()
a = int(a[::-1])
b = int(b[::-1])
if a>b:
    print(a)
else:
    print(b)