import sys
from collections import deque

input = sys.stdin.readline
q = deque()
n, k = map(int, input().split())
visited = [0] * 100001

def bfs(n, k):
  if n > k:
    return n-k
  q.append(n)
  while q:
    now = q.popleft()
    if now == k:
      return visited[k]
    next = [now-1, now+1, now*2]
    for i in next:
      if i <= 100000 and i >= 0 :
        if visited[i] == 0:
          visited[i] = visited[now]+1
          q.append(i)
        
      
print(bfs(n, k))
