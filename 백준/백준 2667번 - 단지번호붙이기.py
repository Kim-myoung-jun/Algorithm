import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
data = []
ans = []
for _ in range(n):
  data.append(list(map(int, input().strip())))

def find(i ,j):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  cnt = 0

  q = deque()
  q.append((i, j))
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
    
      if nx>=n or nx<0 or ny>=n or ny<0:
        continue
      if data[nx][ny] == 1:
        cnt += 1
        data[nx][ny] = 2
        q.append((nx, ny))

  if cnt == 0:
    cnt += 1
  return cnt

for i in range(n):
  for j in range(n):
    if data[i][j] == 1:
      ans.append(find(i, j))

print(len(ans))
ans.sort()
for i in ans:
  print(i)
