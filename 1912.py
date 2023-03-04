import sys
n = int(input())

al = list(map(int,sys.stdin.readline().split()))

dp = [0] * n

for i in range(n):
    a = al[i]
    for j in range(i+1,n):
        if al[j] < 0:
            break
        else:
            a += al[j]
    dp[i] = a

print(max(dp))