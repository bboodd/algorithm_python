n = int(input())
s = ['']*50
a=[]
for _ in range(n):
    a.append(input())
a.sort(key=len)

for i in a:
    s[len(i)].append(i)
    print(len(i))

print(s[1])
print(a)