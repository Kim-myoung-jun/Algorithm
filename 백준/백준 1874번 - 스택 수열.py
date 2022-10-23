import sys
n = int(sys.stdin.readline())

stack = []
result = []
count = 0
flag = True
for _ in range(n):
  a = int(sys.stdin.readline())
  if count < a:
    for i in range(count, a):
      stack.append(i+1)
      result.append("+")
    stack.pop()
    result.append("-")
    count = a
  else:
    b = stack.pop()
    if b != a:
      print("NO")
      flag = False
      break
    else:
      result.append("-")
if flag:
  for i in result:
    print(i)
