import sys
input = sys.stdin.readline
from collections import deque

n,m,start = map(int, input().strip().split(" "))

graph = [ [] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

visited = [0]*(n+1)

def bfs(graph, start):
    visited = [0]*(n+1)
    visited[start] = 1
    q = deque()
    q.append(start)
    while q:
        start = q.popleft()
        print(start,end = " ")
        for i in graph[start]:
            if visited[i] == 0 :
                q.append(i)
                visited[i] = 1

def dfs(graph, start, visited):
    print(start, end = " ")
    visited[start]=1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(graph, i, visited)


dfs(graph, start, visited)
print("")
bfs(graph, start)
