import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().strip())))
    
q = deque()
q.append((0, 0))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while q:
    now = q.popleft()
    now_x = int(now[0])
    now_y = int(now[1])
    value = data[now_x][now_y]
    for i in range(4):
        next_x = now_x + dx[i]
        next_y = now_y + dy[i]
        
        if next_x >= n or next_x < 0 or next_y >= m or next_y < 0:
            continue
        if data[next_x][next_y] == 1:
            data[next_x][next_y] = value+1
            q.append((next_x, next_y))
            
print(data[n-1][m-1])
