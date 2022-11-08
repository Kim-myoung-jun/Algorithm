# https://www.acmicpc.net/problem/9461

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
  d = [0] * 101
  d[1] = 1
  d[2] = 1
  d[3] = 1
  k = int(input())
  for i in range(4, k+1):
    d[i] = d[i-3] + d[i-2]
  print(d[k])
