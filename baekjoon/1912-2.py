import sys
n = int(input())

al = list(map(int,sys.stdin.readline().split()))

dp = [0] * n
dp[0] = al[0]
for i in range(1,n):
    dp[i] = max(al[i], dp[i-1] + al[i])

print(max(dp))