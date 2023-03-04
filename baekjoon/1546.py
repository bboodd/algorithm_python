import sys

a = int(input())
x=list(map(int, sys.stdin.readline().split()))
b = max(x)

for i in range(a) :
    x[i] = x[i]/b*100

print(sum(x)/a)