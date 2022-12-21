import sys
input = sys.stdin.readline

cnt = 0
n = int(input())
for _ in range(n):
  s = input().strip()
  stack = []
  for i in s:
    if not stack:
      stack.append(i)
    else:
      top = stack[-1]
      if top == i:
        stack.pop()
      else:
        stack.append(i)
  if not stack:
    cnt+=1
print(cnt)
      
