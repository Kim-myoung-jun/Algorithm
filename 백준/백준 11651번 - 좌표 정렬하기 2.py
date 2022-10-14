import sys
n = int(sys.stdin.readline())
data = []
for _ in range(n):
  x, y = map(int, sys.stdin.readline().split())
  data.append((x, y))

data.sort(key=lambda x:x[0])
data.sort(key=lambda y:y[1])

for i in data:
  print(i[0], i[1])
