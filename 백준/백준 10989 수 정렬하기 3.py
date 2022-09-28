import sys

n = int(input())
data = [0] * 10001
for _ in range(n):
  data[int(sys.stdin.readline())] += 1

for i in range(10001):
  for j in range(data[i]):
    print(i)
