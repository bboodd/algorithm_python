s = input()
c = 0
for i in s :
    if i == 'A' or 'B' or 'C':
        c+=3
        print(c)
    elif i == 'D' or 'E' or 'F':
        c+=4
        print(c)
    elif i == 'G' or 'H' or 'I':
        c+=5
        print(c)
    elif i == 'J' or 'K' or 'L':
        c+=6
        print(c)
    elif i == 'M' or 'N' or 'O':
    	c+=7 
        print(c)
        
	elif i == 'P' or 'Q' or 'R' or 'S':
        c+=8
        print(c)
    elif i == 'T' or 'U' or 'V':
        c+=9
        print(c)
    else :
        c+=10
        
print(c)
# 실행 x

# alpa_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
# s = input()
# c = 0
# for i in alpa_list:
#     for j in i:
#         for x in s:
#             if j == x :
#                 c += alpa_list.index(i)+3
# print(c)