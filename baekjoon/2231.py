a = int(input())
t_a = a
c = 0
for i in range(a):
    a -= 1
    a_list = list(map(int,str(a)))
    b = 0
    for z in range(len(a_list)):
        b += a_list[z]
    if a+b == t_a:
    	c = a
if c == 0 :
    print(int(0))
else:
    print(c)