import sys
input = sys.stdin.readline 
from collections import deque
sys.setrecursionlimit(10000)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    queue = deque((v))
    visited[v] = True
    while queue:
        start = queue.popleft()
        for i in graph[start]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

n,m = map(int, input().strip().split())
graph = [ [] for _ in range(n+1)]
visited = [0] * (n+1)
count = 0

for i in range(m):
    a, b = map(int, input().strip().split(" "))
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)
