import sys

n = int(sys.stdin.readline())
data = []
for i in range(n):
  data.append(sys.stdin.readline().strip())

set_data = set(data)
data = list(set_data)
data.sort()
data.sort(key = len)
for i in data:
  print(i)
