import sys
input = sys.stdin.readline
n, m = map(int, input().split())

stack = []
def dfs(start):
  if len(stack) == m:
    for i in range(m):
      print(stack[i], end=' ')
    print()
    return
  for i in range(start, n+1):
    if i not in stack:
      stack.append(i)
      dfs(i)
      stack.pop()
dfs(1)
