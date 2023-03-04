s = input()
cs = ['c=','c-','dz=','d-','lj','nj','s=','z=']
c = len(s)
n =0
for i in cs:
    n += s.count(i)
print(c-n)
    