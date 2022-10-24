# https://www.acmicpc.net/problem/2805

import sys
n, m = map(int, sys.stdin.readline().split())

data = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(data)
result = 0
while start <= end:
  mid = (start + end) // 2
  length = 0
  for i in data:
    if i > mid:
      length += i - mid
  if length == m:
    result = mid
    break
  if length > m:
    result = mid
    start = mid + 1
  else:
    end = mid - 1

print(result)
