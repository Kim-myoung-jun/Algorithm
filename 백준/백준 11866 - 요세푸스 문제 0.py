import sys
from collections import deque

queue = deque()

n, k = map(int, sys.stdin.readline().split())
data = []
for i in range(n):
    queue.append(i+1)
print("<",end='')
while queue:
    for _ in range(k-1):
        tmp = queue[0]
        queue.popleft()
        queue.append(tmp)
        
    if(len(queue) == 1):
        print(queue[0], end='')
    else:
        print(queue[0], end=', ')
    queue.popleft()
print(">")
