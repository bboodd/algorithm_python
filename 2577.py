num1 = int(input())
num2 = int(input())
num3 = int(input())

num_list = list(str(num1*num2*num3))

a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in num_list:
    a[int(i)] += 1

for i in range(9):
    print(a[i])