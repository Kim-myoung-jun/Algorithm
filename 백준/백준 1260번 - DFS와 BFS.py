# https://www.acmicpc.net/problem/1260

import sys
from collections import deque
q = deque()
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [ [] for i in range(n+1)]
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

def dfs(now):
  visited_dfs[now] = True
  print(now, end=' ')
  graph[now].sort()
  for i in graph[now]:
    if not visited_dfs[i]:
      dfs(i)
      
def bfs(now):
  visited_bfs[now] = True
  q.append(now)
  while q:
    v = q.popleft()
    print(v, end=' ')
    graph[v].sort()
    for i in graph[v]:
      if not visited_bfs[i]:
        q.append(i)
        visited_bfs[i] = True
  
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

dfs(v)
print()
bfs(v)
