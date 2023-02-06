import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = []
for i in range(n):
  arr.append(list(map(int, input().split())))

x, y, size, cnt = 0, 0, 2, 0
for i in range(n):
  for j in range(n):
    if arr[i][j] == 9:
      x, y = i, j
      arr[x][y] = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def find_fish(x, y, size):
  visited = [[0] * n for _ in range(n)]
  distance = [[0]*n for _ in range(n)]
  q = deque()
  #현재 위치 저장
  q.append((x, y))
  visited[x][y] = 1
  temp = []
  while q:
    now_x, now_y = q.popleft()
    for i in range(4):
      #4방향 확인하며 먹을 수 있는 물고기 찾기
      nx = now_x + dx[i]
      ny = now_y + dy[i]
      #방문하지 않은 좌표
      if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
        #지나갈 수 있으면(상어보다 크기가 같거나 작은)
        if arr[nx][ny] <= size:
          #지나감
          q.append((nx, ny))
          visited[nx][ny] = 1
          distance[nx][ny] = distance[now_x][now_y] + 1
          #먹을 수 있으면(상어보다 크기가 작으며, 0이 아님)
          if 0 < arr[nx][ny] < size:
            #좌표, 거리 리스트에 담기
            temp.append((nx, ny, distance[nx][ny]))
  #거리가 가까운, 위, 왼쪽순 정렬
  return sorted(temp, key = lambda x : (-x[2], -x[0], -x[1]))
  
result = 0
fish = 0
while True:
  fish = find_fish(x, y, size)
  if len(fish) == 0:
    break
  nx, ny, dist = fish.pop()
  result += dist
  arr[x][y], arr[nx][ny] = 0, 0
  x,y = nx,ny
  cnt += 1
  if size == cnt:
    size += 1
    cnt = 0
print(result)
  
