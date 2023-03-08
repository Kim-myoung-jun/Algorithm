import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
visited = [ False for _ in range(n+1)]
data = [ []  for _ in range(n+1)]
result = [ 0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)
    
def dfs():
    q = deque()
    q.append(1)
    visited[1] = True
    while q:
        now = q.popleft()
        if visited[now] == True:
            for i in data[now]:
                q.append(i)
                result[i] = now
        else:
            visited[now] = True
            for i in data[now]:
                if visited[i] == False:
                    q.append(i)
                else:
                    if result[now] == 0:
                        result[now] = i
                
dfs()
for i in range(2, n+1):
    print(result[i])
