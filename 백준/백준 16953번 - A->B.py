# bfs 사용
import sys
from collections import deque
input = sys.stdin.readline
a, b = map(int, input().split())

q = deque()
q.append((a, 1))
flag = False
while(q):
    n, cnt = q.popleft()
    if n > b:
        continue
    if n == b:
        print(cnt)
        flag = True
        break
    q.append( (int(str(n)+"1"), cnt+1))
    q.append((n*2, cnt+1))
if flag == False:
    print(-1)
    
# Top Down 사용
'''
import sys
from collections import deque
input = sys.stdin.readline
a, b = map(int, input().split())
cnt = 1
while b != a:
    cnt += 1
    tmp = b
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    if tmp == b:
        print(-1)
        break
else:
    print(cnt)
'''
