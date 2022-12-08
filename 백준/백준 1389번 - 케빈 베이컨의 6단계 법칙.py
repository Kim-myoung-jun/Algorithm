import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [ [INF] * (n+1) for _ in range(n+1) ]
for i in range(1, n+1):
  graph[i][i] = 0

for i in range(0, m):
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(a+1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
      graph[b][a] = graph[a][b]

comp = INF
for i in range(1, n+1):
  row_sum = 0
  for j in range(1, n+1):
    row_sum += graph[i][j]
  if comp > row_sum:
    ans = i
    comp = row_sum
print(ans)
