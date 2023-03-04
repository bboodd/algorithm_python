import sys

n = int(sys.stdin.readline())
a = []
count = 1

for i in range(n):
    a.append(list(map(int,sys.stdin.readline().split())))

a.sort(key=lambda x:(x[1],x[0]))
last = a[0][1]

for i in range(1,n):
    if a[i][0] >= last:
        last = a[i][1]
        count+=1
print(count)
    