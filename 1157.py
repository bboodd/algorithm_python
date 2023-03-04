word = input().lower() 
word_list = list(set(word))
cnt = []
for i in word_list:
    ccount = word.count(i)
    cnt.append(ccount)
if cnt.count(max(cnt)) >1:
    print("?")
else :
    print(word_list[cnt.index(max(cnt))].upper())
# word = input() 
# s = list(0 for i in range(0,26))

# for i in word.upper():
#     s[ord(i)-65] +=1
# if s.count(max(s)) <2:
#     print(chr(s.index(max(s))+65))
# else :
#     print("?")