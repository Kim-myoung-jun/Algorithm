import sys
input = sys.stdin.readline

a, b = map(int, input().split())

def foo(x, y):
  r = x%y
  x = y
  y = r
  while r:
    r = x%y
    x = y
    y = r
  return x
print("1"*foo(a, b))
