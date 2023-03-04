n = [500, 100, 50, 10, 5, 1]

a = 1000-int(input())
count = 0 
for i in n:
    if a >= i:
        count+=a//i
        a %= i
print(count)