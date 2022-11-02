# https://www.acmicpc.net/problem/11399

import sys
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

data.sort()
result = 0
data2 = []
for i in range(n):
  result += data[i]
  data2.append(result)
print(sum(data2))
