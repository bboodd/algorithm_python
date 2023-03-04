# s = input()
# c = 0
# a = list(-1 for i in range(0,24))
# for i in s :
#     if a[ord(i) - 97] == -1:
#     	a[ord(i) - 97] = c
#     	c+=1
#     else :
#         c+=1
# print(a)
word = input()
alphabet = list(range(97,123))  # 아스키코드 숫자 범위

for x in alphabet :
    print(word.find(chr(x))) 