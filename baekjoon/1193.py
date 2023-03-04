# 1  2  6  7  15 16 28
# 3  5  8  14 17 27
# 4  9  13 18 26
# 10 12 19 25
# 11 20 24
# 21 23
# 22
a = int(input())
n = 1
c = 2
p = 1
pp = 1
while 1:
    if a == 1 :
        print (str(1)+'/'+str(1))
        break
    elif p < a and a <= n :
        print(str(a-p))
        #print(str((a-((a-p-1)*2+pp)))+'/'+str((a-p)))
        break
    elif n < a and a <= n+c+1 :
        print(a)
        print(n)
        print(str((a-n))+'/'+str(((n+c+1)-a+1)))
        break
    else :
        pp = p
        n += c
        c += 1
        p = n
        
X=int(input())

line=1
while X>line:
    X-=line
    line+=1
    
if line%2==0:
    a=X
    b=line-X+1
else:
    a=line-X+1
    b=X
    
print(a, '/', b, sep='')
        
#          n += c 1 3 6 10 15
#         c +=    1 2 3 4 5  6
        #   p =   1 1 3 6 10
#         1 3 5
#         6 8 10 12 14
#         15 17 19 21 23 25 27
# 0 3 10 21
# 1 6 15