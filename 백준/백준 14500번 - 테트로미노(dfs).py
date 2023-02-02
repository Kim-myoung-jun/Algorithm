import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = []
for _ in range(n):
  data.append(list(map(int, input().split())))

val = 0
#위/오른쪽/아래/왼쪽 시계방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [ [0] * m for _ in range(n)]

def dfs(x, y, index, total):
  global val
  if index == 3:
    val = max(val, total)
    return
  else:
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
        if index == 1:
          visited[nx][ny] = 1
          dfs(x, y, index+1, total + data[nx][ny])
          visited[nx][ny] = 0
        visited[nx][ny] = 1
        dfs(nx, ny, index+1, total+data[nx][ny])
        visited[nx][ny] = 0
        
for i in range(n):
  for j in range(m):
    visited[i][j] = 1
    dfs(i, j, 0, data[i][j])
    visited[i][j] = 0
print(val)
