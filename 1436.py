n = int(input())
num = 0
m = 666
while n != num:
    count = 0
    for i in str(m):
        if i == '6':
            count+=1
            if count == 3:
                num+=1
                if num == n:
                    print(m)
        else:
            count = 0
    m+=1
