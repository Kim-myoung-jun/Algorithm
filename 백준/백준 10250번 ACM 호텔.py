t = int(input())

for _ in range(t):
  h, w, n = map(int, input().split())
  if n%h == 0:
    y = h
    x = str(int(n/h))
  else:
    y = n%h
    x = str(int(n/h)+1)
  if int(x) < 10:
    x = '0'+x
  print(str(y)+x)
