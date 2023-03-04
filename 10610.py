a = list(input())

a.sort(reverse=True)
s = 0
for i in a:
    s+=int(i)
if '0' not in a or s % 3 != 0:
    print(-1)
else:
    print(''.join(a))