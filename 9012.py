n = int(input())
x = '('
y = ')'
m = []

for _ in range(n):
    count = 0
    a = input()
    for i in a:
        if i == x:
            count+=1
        else:
            if count == 0:
                count -= 100
            else:
                count -= 1
    if count == 0:
        #print('YES')
        m.append('YES')
    else:
        m.append('NO')
        #print('NO')
for i in range(n):
    print(m[i])