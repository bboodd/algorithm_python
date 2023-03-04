num1 = int(input())
num2 = 99
if num1 < 100 :
    print(num1)
else :
    for i in range(100,num1+1):
        li = list(map(int,str(i)))
        if (li[1] - li[0]) == (li[2] - li[1]):
            num2+=1
    print(num2)