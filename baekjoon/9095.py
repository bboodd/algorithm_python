n = int(input())

dp = [0] * 12

def onetwothree(m):
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4,m+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[m]

for _ in range(n):
    a = int(input())
    print(onetwothree(a))