n=input()

num = ''
p = 0
m = 0
m_c = 0

for i in n:
    if i =='-':
        if m_c == 1:
            m+=int(num)
            num = ''
        else:
            p+=int(num)
            m_c = 1
            num = ''
    elif i == '+':
        if m_c == 1:
            m+=int(num)
            num = ''
        else:
            p+=int(num)
            num = ''
    else:
        num+=i
if m_c == 1:
    m+=int(num)
else:
    p+=int(num)

print(p-m)
            
        
        