n = int(input())

i=0
if n == 1:
  print(1)
else:
  while True:
    k = 3*i*(i+1)+1
    if k>=n:
      print(i+1)
      break
    i += 1
