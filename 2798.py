N,M = map(int,input().split())
card = list(map(int,input().split()))
a = 0

for x in range(N):
    for y in range(x+1,N):
        for z in range(y+1,N):
            if card[x] + card[y] + card[z] > M:
                continue
            else:
                a = max(a,card[x]+card[y]+card[z])
print(a)