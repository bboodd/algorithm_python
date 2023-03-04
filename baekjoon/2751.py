import sys

n = int(sys.stdin.readline())
a = []
for _ in range(n):
    a.append(int(sys.stdin.readline()))
    
a.sort()
a = tuple(a)

for i in range(n):
    print(a[i])