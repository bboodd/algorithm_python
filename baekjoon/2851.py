a = []
s = 0
for i in range(10):
    a.append(int(input()))
    
for j in a:
    s+=j
    if s >= 100:
        if s - 100 > 100 - (s - j):
            s -= j
        break
print(s)
    