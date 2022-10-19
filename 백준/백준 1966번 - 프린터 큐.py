# https://www.acmicpc.net/problem/1966
import sys
from collections import deque

k = int(sys.stdin.readline())
for _ in range(k):
  n, m = map(int, sys.stdin.readline().split())
  q = deque(list(map(int, sys.stdin.readline().split())))
  count = 0
  while q:
    best = max(q)
    first = q.popleft()
    m -= 1
    
    if best == first:
      count += 1
      if m < 0:
        print(count)
        break
    else:
      q.append(first)
      if m < 0:
        m = len(q)-1
