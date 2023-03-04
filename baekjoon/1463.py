n = int(input())
count = 0
def m1(m):
    global count
    if m == 1:
        return 1
    else:
        if m % 3 == 0:
            count +=1
            m1(m // 3)
        elif m % 2 == 0:
            if m // 2 == 5:
                count+=1
                m1(m-1)
            else:
                count +=1
                m1(m//2)
        else:
            count+=1
            m1(m-1)
m1(n)
print(count)