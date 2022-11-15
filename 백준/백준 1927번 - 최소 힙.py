# https://www.acmicpc.net/problem/1927

import sys
input = sys.stdin.readline

import heapq
n = int(input())
q = []
for _ in range(n):
  a = int(input())
  if a == 0:
    if q:
      print(heapq.heappop(q))
    else:
      print(0)
  else:
    heapq.heappush(q, a)
