import sys
from collections import deque


n,m,r= map(int,sys.stdin.readline().split())

graph = [ [] for i in range(n+1)]

visited = [0] * (n+1)

cnt = 1

for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(r):
    global cnt
    
    q = deque([r])
    
    visited[r] = cnt
    
    while q:
        v = q.popleft()
        graph[v].sort()
        for i in graph[v]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                q.append(i)


bfs(r)

for i in range(n+1):
    if i != 0:
        print(visited[i])