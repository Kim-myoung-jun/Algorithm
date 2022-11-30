import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
data = [ [] * n for _ in range(m)]
q = deque()
for i in range(m):
    lst = list(map(int, input().split()))
    for j in range(n):
        if lst[j] == 1:
            q.append((i, j))
    data[i] = lst
    
def bfs():
    dx = [-1, 1, 0, 0] #상하좌우
    dy = [0, 0 ,-1, 1]
    global q
    cnt = 1
    while q:
        next_q = deque()
        for i in range(len(q)):
            now = q.popleft()
            for j in range(4):
                nx = now[0]+dx[j]
                ny = now[1]+dy[j]
                if(nx < 0 or nx >= m or ny < 0 or ny >= n):
                    continue
                if data[nx][ny] == 0:
                    data[nx][ny] = cnt
                    next_q.append((nx, ny))
                    
        q = next_q
        cnt+=1
                
    for i in range(m):
        if data[i].count(0):
            return -1
    return cnt-2

print(bfs())
'''
for i in range(m):
    for j in range(n):
        print(data[i][j], end=' ')
    print()
'''    
