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
  
