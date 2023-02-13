import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
visited = [0] * n
stack = []
def dfs(start, index):
  if index == m:
    for i in range(m):
      print(stack[i], end=' ')
    print()
    return
  for i in range(0, n):
    if data[i] not in stack:
      stack.append(data[i])
      dfs(i+1, index+1)
      stack.pop()

dfs(0, 0)
