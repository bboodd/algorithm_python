import sys
n = int(input())

distance = list(map(int,sys.stdin.readline().split()))
price = list(map(int,sys.stdin.readline().split()))
total = 0
t_d = 0
m_p = price[0]

for i in range(n-1):
    if price[i] >= m_p:
        t_d += distance[i]
        
    else:
        total += t_d * m_p
        t_d = distance[i]
        m_p = price[i]
total+=t_d*m_p        
print(total)