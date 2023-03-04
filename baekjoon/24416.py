n = int(input())
count = [0] * 2
def fib(n):
    if n == 1 or n == 2: # 코드 1
        count[0]+=1
        return 1
    return fib(n - 1) + fib(n - 2)
fib(n)
f = [0] * (n + 1)
def fibonacci(n):
    f[1] = 1
    f[2] = 1
    for i in range(3, n+1):
        count[1] += 1
        f[i] = f[i - 1] + f[i - 2]  # 코드2
    return f[n]
fibonacci(n)
print(count[0],count[1])
