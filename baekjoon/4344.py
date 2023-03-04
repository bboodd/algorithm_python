import sys

a = int(input())
for i in range(a):
    x = list(map(int,sys.stdin.readline().split()))
    y = sum(x[1:])/x[0]
    b = 0
    for i in x[1:]:
        if i>y:
            b+=1
    print(f'{b*100/x[0]:.3f}%')