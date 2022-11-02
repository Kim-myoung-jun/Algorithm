# https://www.acmicpc.net/problem/17219

import sys
n, m = map(int, sys.stdin.readline().split())

dict = {}
for i in range(n):
  a, b = map(str, sys.stdin.readline().rstrip().split())
  dict[a] = b

for _ in range(m):
  q = sys.stdin.readline().rstrip()
  print(dict.get(q))
