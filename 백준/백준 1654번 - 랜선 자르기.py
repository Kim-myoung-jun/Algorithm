# https://www.acmicpc.net/problem/1654

import sys
k, n = map(int, sys.stdin.readline().split())
line = []
for _ in range(k):
  line.append(int(sys.stdin.readline()))

start = 1
end = max(line)

while start <= end:
  mid = (start + end) // 2
  length = 0
  for i in line:
    length += i // mid
  if length < n:
    end = mid -1
  else:
    start = mid+1
print(end)
