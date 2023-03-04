n = int(input())

dp = [0] * 91

def fib(m):
    dp[1] = 1
    dp[2] = 1
    for i in range(3,m+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[m]
print(fib(n))
    