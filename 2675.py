
a = int(input())

for i in range(a):
    b,c = input().split()
    text = ''
    for i in c:
        text+= int(b)*i
    print(text)