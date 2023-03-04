e,s,m = map(int,input().split())

year = 1

x,y,z = 1,1,1

while True:
    if x == e and y == s and z == m:
        break
    else:
        x +=1
        y +=1
        z +=1
        if x > 15:
            x = 1
        if y > 28:
            y = 1
        if z > 19:
            z = 1
    year+=1
print(year)