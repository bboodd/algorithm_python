import sys
sys.setrecursionlimit(10 ** 6) 

n,m,r= map(int,sys.stdin.readline().split())

graph = [ [] for i in range(n+1)]

visited = [0] * (n+1)

cnt = 1

def dfs(graph, v, visited):
    global cnt
    
    visited[v] = cnt
    
    for i in graph[v]:
        if visited[i] ==0:
            cnt+=1
            dfs(graph, i, visited)

for i in range(m):
    x,y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(n+1):
    graph[i].sort()
    
dfs(graph,r,visited)

for i in range(n+1):
    if i != 0:
        print(visited[i])