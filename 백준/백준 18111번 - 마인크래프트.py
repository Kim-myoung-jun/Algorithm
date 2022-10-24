# https://www.acmicpc.net/problem/18111

import sys
import math
n, m, b = map(int, sys.stdin.readline().split())
data = []
for _ in range(n):
  data.append(list(map(int, sys.stdin.readline().split())))

time = 0
avg = 0
max_block = 0
min_block = 256
for i in range(n):
  avg += sum(data[i])
  
  tmp_max = max(data[i])
  max_block = max(tmp_max, max_block)

  tmp_min = min(data[i])
  min_block = min(tmp_min, min_block)
avg = round(avg/(n*m))
print(max_block, min_block, avg)

check = []
for i in range(n):
  for j in range(m):
    if data[i][j] > avg:
      c = data[i][j] - avg
      time += 2 * c
      b += 1 * c
    elif data[i][j] < avg:
      c = avg - data[i][j]
      time += 1 * c
      b -= 1 * c

if b < 0:
  tmp_avg = avg + b
  time = 0
  for i in range(n):
    for j in range(m):
      if data[i][j] > tmp_avg:
        time += (data[i][j] - tmp_avg) * 2
      elif data[i][j] < tmp_avg:
        time += (tmp_avg - data[i][j])
  avg = tmp_avg
print(time, avg)
