n = int(input())

def func(m): # 시간 초과
    if m == 1 or m == 2 or m == 3:
        return 1
    if m == 4 or m == 5:
        return 2
    if dp[m] != 0:
        return dp[m]
    else:
        return func(m-1) + func(m-5)
    return dp[m]

def func2(m): # 통과
    dp[1],dp[2],dp[3] = 1,1,1
    dp[4],dp[5] = 2,2
    for i in range(6,m+1):
        dp[i] = dp[i-1] + dp[i-5]
    return dp[m]

dp = [0] * 101

for _ in range(n):
    a = int(input())
    print(func(a))
    print(func2(a))
    
