n = int(input())
a = 2
'''
if n != 1:
  while True:
    if n % a == 0:
      print(a)
      n = n // a
    elif n % a != 0:
      a += 1
    
    if n == 1:
      break
''' #2000ms
'''
while a <= n:
  if n % a == 0:
    print(a)
    n = n // a
  else:
    a += 1
''' #1400ms

while a <= int(n ** 0.5):
  if n % a == 0:
    print(a)
    n //= a
  else:
    a += 1
if n > 1:
  print(n)
  #60ms
