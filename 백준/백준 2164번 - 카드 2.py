from collections import deque
import sys
n = int(sys.stdin.readline())

queue = deque()
for i in range(n):
    queue.append(i+1)
    
while len(queue)>1:
    queue.popleft()
    tmp = queue.popleft()
    queue.append(tmp)
    
print(queue.popleft())
