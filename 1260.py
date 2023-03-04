# import sys
# # dfs = 스택 bfs = 큐

# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end=' ')
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i , visited)
            
# a,b,c = map(int,sys.stdin.readline().split())
# visited = [False] * (a+1)
# graph = [[0]]*(a+1)


# for _ in range(b):
#     x,y = map(int,input().split())
#     if graph[x][0] == 0:
#         graph[x] = y
#     else:
#         graph[x].append(y)
    
# dfs(graph, c, visited)
from collections import deque
import sys
read = sys.stdin.readline

def bfs(v):
    q = deque()
    q.append(v)
    visit_list[v] = 1
    while q:
        v = q.popleft()
        print(v,end=' ')
        for i in range(1, n+1):
            if visit_list[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visit_list[i] = 1
    
    
def dfs(v):
    visit_list2[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if visit_list2[i] == 0 and graph[v][i] == 1:
            dfs(i)
    
    

n,m,v = map(int,read().split())

graph = [[0]*(n+1) for _ in range( n+1)]

visit_list = [0]* (n+1)
visit_list2 = [0] * (n+1)

for _ in range(m):
    a,b = map(int,read().split())
    graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)
