a = int(input())

for i in range(1,a+1):
    c = 0
    H,W,N = map(int,input().split())
    c = int((N%H))*100 + int((N//H+1))
    print(c)
    