n = int(input())

arr = []
for _ in range(n):
  arr = input()
  stack = []
  flag = "YES"
  for i in arr:
    if i == '(':
      stack.append(i)
    else:
      if len(stack) == 0:
        flag = "NO"
        break
      else:
        if stack.pop() == i:
          flag = "NO"
          break
  if len(stack) > 0:
    print("NO")
  else:
    print(flag)
  
  '''
from sys import stdin

n = int(input())
for _ in range(n):
    str_ = stdin.readline().strip()
    stack = 0
    for chr_ in str_:
        if chr_ == '(':
            stack += 1
        else:
            stack -= 1
            if stack < 0:
                break
    if stack == 0:
        print('YES')
    else:
        print('NO')
'''
