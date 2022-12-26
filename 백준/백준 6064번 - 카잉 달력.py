import sys
input = sys.stdin.readline

t = int(input())

def find(m, n, x, y):
  while x <= m*n:
    if (x-y)%n == 0:
      return x
    else:
      x += m
  return -1

for _ in range(t):
  m, n, x, y = map(int, input().split())
  print(find(m, n, x, y))
