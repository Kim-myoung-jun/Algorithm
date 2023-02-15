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
  for i in range(start, n):
    stack.append(data[i])
    dfs(i, index+1)
    stack.pop()

dfs(0, 0)
