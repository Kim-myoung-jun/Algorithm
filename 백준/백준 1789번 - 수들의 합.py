'''
s = int(input())
a = 1
result = 0
while True:
  result = (a*(a+1))/2
  if result >= s:
    break
  a += 1

if result == s:
  print(a)
elif result - a < s:
  print(a-1)
else:
  print(a)
'''

s = int(input())
n = 1
while n * (n + 1) / 2 <= s:
    n += 1
print(n - 1)
