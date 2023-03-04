x_l = []
y_l = []
x = 0
y = 0
for _ in range(3):
    a,b = map(int,input().split())
    x_l.append(a)
    y_l.append(b)

for i in range(3):
    if x_l.count(x_l[i]) == 1:
        x = x_l[i]
    if y_l.count(y_l[i]) == 1:
        y = y_l[i]
        
print(x,y)