import sys
n = int(input())
a = []

for _ in range(n):
    a.append(int(sys.stdin.readline()))
    
a.sort(reverse=True)
x = a[0]
num = 2
for i in range(1,len(a)):
    if x < a[i] * num:
        x = a[i] * num
    num+=1
print(x)