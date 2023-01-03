import sys
input = sys.stdin.readline
from collections import deque

board = [0] * 101
n, m = map(int, input().split())
up = []
for _ in range(n):
  x, y = map(int, input().split())
  board[x] = y

down = []
for _ in range(m):
  u, v = map(int, input().split())
  board[u] = v

visited = [0] * 101
q = deque()
q.append(1)
while q:
  print(q)
  now = q.popleft()
  if now == 100:
    print(visited[100])
    break
  for i in range(1, 7):
    next = now + i
    if next > 100:
      break
    if board[next] != 0:
      next = board[next]
    if visited[next] == 0:
      visited[next] = visited[now] + 1
      print("next - ",next)
      q.append(next)
