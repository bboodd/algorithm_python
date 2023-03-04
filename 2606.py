from collections import deque

n = int(input())
m = int(input())

visit = [0] * (n+1)
graph = [[]for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a] += [b]
    graph[b] += [a]

visit[1] = 1
q=deque([1])

while q:
    c = q.popleft()
    for x in graph[c]:
        if visit[x] == 0:
            q.append(x)
            visit[x] = 1
print(sum(visit)-1)