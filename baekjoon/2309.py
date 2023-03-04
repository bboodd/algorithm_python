a = []

answer = []
for _ in range(9):
    a.append(int(input()))

a.sort()

sum_a = sum(a)
    
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if sum_a - a[i] - a[j] == 100:
            for k in range(len(a)):
                if k == i or k == j:
                    pass
                else:
                    print(a[k])