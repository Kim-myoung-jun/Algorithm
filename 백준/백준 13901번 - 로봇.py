import sys
input = sys.stdin.readline

r, c = map(int, input().split())
data = [ [0] * c for _ in range(r)]

k = int(input())
for _ in range(k):
  kr, kc = map(int, input().split())
  data[kr][kc] = -1

x, y = map(int, input().split())
data[x][y] = 1

dir = list(map(int, input().split()))

last = [x, y]
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

pos = 0
cnt = 0
while True:
  if cnt == 4:
    break
  pos = pos%4
  nx = x + dx[dir[pos]]
  ny = y + dy[dir[pos]]
  if nx < 0 or nx >= r or ny < 0 or ny >= c or data[nx][ny] != 0:
    pos += 1
    cnt += 1
  else:
    cnt = 0
    data[nx][ny] = data[x][y]+1
    x = nx
    y = ny
    last = [x, y]
print(last[0], last[1])
