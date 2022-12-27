import sys
input = sys.stdin.readline

t= int(input())
for _ in range(t):
  p = input().strip()
  n = int(input())
  s = input().strip()
  s = s[1:len(s)-1]
  if len(s) > 0:
    data = s.split(",")
  else:
    data = []
  flag = 0
  for i in p:
    if i == 'R':
      if flag == 0:
        flag = 1
      else:
        flag = 0
    else:
      if len(data) > 0:
        if flag == 0:
          del data[0]
        else:
          del data[-1]
      else:
        flag = 2
        break
  if flag == 2:
    print("error")
    continue
  elif flag == 1:
    data.reverse()

  print("[", end='')
  for i in range(len(data)):
    print(data[i], end='')
    if i < len(data)-1:
      print(",", end='')
  print("]")
