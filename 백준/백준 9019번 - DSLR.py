import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
  
for _ in range(t):
  a, b = map(int, input().split())
  q = deque()
  visited = [False] * 10001
  visited[a] = True
  q.append((a, ''))
  while q:
    value, letter = q.popleft()
    if value == b:
      print(letter)
      break

    D = 2*value%10000
    if visited[D] == False:
      q.append((D, letter+'D'))
      visited[D] = True

    if value == 0:
      S = 9999
    else:
      S = value-1
    if visited[S] == False:
      q.append((S, letter+'S'))
      visited[S] = True

    L = 10*(value%1000) + value//1000
    if visited[L] == False:
      q.append((L, letter+'L'))
      visited[L] = True

    R = 1000*(value%10) + value//10
    if visited[R] == False:
      q.append((R, letter+'R'))
      visited[R] = True
  
  
