def fibo(n):
    result = 1
    if n >= 2:
        result = fibo(n-1) + fibo(n-2)
    elif n == 1:
        return result
    elif n == 0:
        return 0
    return result

n = int(input())

print(fibo(n))