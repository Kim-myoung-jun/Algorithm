import sys
input = sys.stdin.readline
from collections import deque

m, n, h = map(int, input().split())
data = []
q = deque()

for k in range(h):
  tmp = []
  for i in range(n):
    tmp.append(list(map(int, input().split())))
    for j in range(m):
      if tmp[i][j] == 1:
        q.append((i, j, k))
  data.append(tmp)

def bfs():
  dx = [-1, 1, 0, 0, 0, 0] #x축 위 아래
  dy = [0, 0, -1, 1, 0, 0] #y축 왼쪽 오른쪽
  dz = [0, 0, 0, 0, 1, -1] #z축 위 아래
  global q
  cnt = 1
  while q:
    next_q = deque()
    for _ in range(len(q)):
      x, y, z = q.popleft()
      for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and data[nz][nx][ny] == 0:
          data[nz][nx][ny] = cnt
          next_q.append((nx, ny, nz))
    q = next_q
    cnt+=1

  for i in data:
    for j in i:
      for k in j:
        if k == 0:
          return -1
  return cnt-2

print(bfs())
'''
import sys
input = sys.stdin.readline
from collections import deque

m, n, h = map(int, input().split())
data = []
q = deque()

for i in range(h):
  tmp = []
  for j in range(n):
    tmp.append(list(map(int, input().split())))
    for k in range(m):
      if tmp[j][k] == 1:
        q.append((i, j, k))
  data.append(tmp)

dx = [-1, 1, 0, 0, 0, 0] #x축 위 아래
dy = [0, 0, -1, 1, 0, 0] #y축 왼쪽 오른쪽
dz = [0, 0, 0, 0, 1, -1] #z축 위 아래

while q:
  x, y, z = q.popleft()
  for i in range(6):
    a = x+dx[i]
    b = y+dy[i]
    c = z+dz[i]
    if 0<=a<h and 0<=b<n and 0<=c<m and data[a][b][c]==0:
      q.append([a,b,c])
      data[a][b][c] = data[x][y][z]+1

day = 0
for i in data:
  for j in i:
    for k in j:
      if k == 0:
        print(-1)
        exit(0)
    day = max(day, max(j))
print(day-1)
'''
