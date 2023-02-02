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

def get_4x1(x, y, dir):
  cnt = 0
  for i in range(4):
    nx = x + dx[dir] * i
    ny = y + dy[dir] * i
    if 0 > nx or 0 > ny or nx >= n or ny >= m:
      return 0
    cnt += data[nx][ny]
  return cnt

def get_2x2(x, y):
  nx = x + 1
  ny = y + 1
  if nx >= n or ny >= m:
    return 0
  cnt = data[x][y]
  cnt += data[nx][y]
  cnt += data[x][ny]
  cnt += data[nx][ny]
  return cnt

def get_L(x, y, dir):
  cnt = 0
  for i in range(3):
    nx = x + dx[dir] * i
    ny = y + dy[dir] * i
    if 0 > nx or 0 > ny or nx >= n or ny >= m:
      return 0
    cnt += data[nx][ny]
  c1 = c2 = 0
  if dir % 2 == 0: #위나 아래방향이면
    tmp1 = ny+1
    if tmp1 < m:
      c1 = data[nx][tmp1]
    tmp2 = ny-1
    if tmp2 >= 0:
      c2 = data[nx][tmp2]
  else:
    tmp1 = nx+1
    if tmp1 < n:
      c1 = data[tmp1][ny]
    tmp2 = nx-1
    if tmp2 >= 0:
      c2 = data[tmp2][ny]
  if c1 == 0 and c2 == 0:
    return 0
  cnt += max(c1, c2)
  return cnt
    
def get_Z(x, y, dir):
  cnt = 0
  for i in range(2):
    nx = x + dx[dir] * i
    ny = y + dy[dir] * i
    if 0 > nx or 0 > ny or nx >= n or ny >= m:
      return 0
    cnt += data[nx][ny]
    
  c1 = c2 = 0
  if dir % 2 == 0: #위나 아래방향이면
    left = ny-1
    right = ny+1
    if 0<= left:
      c1 = data[nx][left]
      nnx = nx+dx[dir]
      if 0 <= nnx < n:
        c1 += data[nnx][left]
      else:
        c1 = 0
    if right < m:
      c2 = data[nx][right]
      nnx = nx+dx[dir]
      if 0 <= nnx < n:
        c2 += data[nnx][right]
      else:
        c2 = 0
  else:
    up = nx -1
    down = nx+1
    if 0 <= up:
      c1 = data[up][ny]
      nny = ny+dy[dir]
      if 0<=nny<m:
        c1 += data[up][nny]
      else:
        c1 = 0
    if down < n:
      c2 = data[down][ny]
      nny = ny+dy[dir]
      if 0 <= nny < m:
        c2 += data[down][nny]
      else:
        c2 = 0
  if c1 == 0 and c2 == 0:
    return 0
  cnt += max(c1,c2)
  return cnt

def get_jk(x, y, dir):
  cnt = 0
  for i in range(2):
    nx = x + dx[dir] * i
    ny = y + dy[dir] * i
    if 0 > nx or 0 > ny or nx >= n or ny >= m:
      return 0
    cnt += data[nx][ny]
  tmpx = nx + dx[dir]
  tmpy = ny + dy[dir]
  if 0>tmpx or 0>tmpy or tmpx>=n or tmpy>=m:
    return 0
  cnt += data[tmpx][tmpy]

  c1 = c2 = 0
  if dir % 2 == 0: #위나 아래방향이면
    left = ny-1
    right = ny+1
    if 0 <= left:
      c1 = data[nx][left]
    if right < m:
      c2 = data[nx][right]
  else:
    up = nx -1
    down = nx+1
    if 0 <= up:
      c1 = data[up][ny]
    if down < n:
      c2 = data[down][ny]
  if c1 == 0 and c2 == 0:
    return 0
  cnt += max(c1, c2)
  return cnt   
  
sum = 0
for i in range(n):
  for j in range(m):
    case2 = get_2x2(i, j)
    for k in range(4): #시계방향
      case1 = get_4x1(i, j, k)
      case3 = get_L(i, j, k)
      case4 = get_Z(i, j, k)
      case5 = get_jk(i, j, k)

      sum = max(sum, case1, case2, case3, case4, case5)
print(sum)
