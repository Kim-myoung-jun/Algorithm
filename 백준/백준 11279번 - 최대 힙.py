# https://www.acmicpc.net/problem/11279

import sys
import heapq

input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
  a = int(input())
  if a==0:
    if q:
      print(heapq.heappop(q) * -1)
    else:
      print(0)
  else:
    heapq.heappush(q, a*-1)
