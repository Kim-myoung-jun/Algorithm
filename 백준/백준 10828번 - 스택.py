import sys
n = int(sys.stdin.readline())
stack = []
for _ in range(n):
  command = sys.stdin.readline().strip()
  if "push" in command:
    arr = command.split()
    stack.append(arr[1])
  elif command == "pop":
    if len(stack) > 0:
      print(stack.pop())
    else:
      print(-1)
  elif command == "size":
    print(len(stack))
  elif command == "empty":
    if len(stack) > 0:
      print(0)
    else:
      print(1)
  elif command == "top":
    if len(stack) > 0:
      print(stack[len(stack)-1])
    else:
      print(-1)
