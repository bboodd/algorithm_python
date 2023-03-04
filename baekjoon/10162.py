a,b,c = 0,0,0
t = int(input())
if t % 10 != 0:
    print(-1)
else:
    for i in range(3):
        if t >= 300:
            a+= t // 300
            t %=300
        elif t >= 60:
            b += t // 60
            t %= 60
        else:
            c += t // 10
            t %= 10
    print(a,b,c)
        