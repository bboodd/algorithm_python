import sys

a = int(input())

for i in range(a):
    x = list(input())
    sum = 0
    c = 1
    for i in x:
        if i =='O':
            sum+=c
            c+=1
        else:
            c=1
    print(sum)