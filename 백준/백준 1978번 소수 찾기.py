import sys
n = int(sys.stdin.readline())
data = map(int, input().split())
cnt = 0

def find(x):
  for i in range(2, x):
    if x % i == 0:
      return False
  return True

for i in data:
  if i == 1:
    continue
  if find(i):
    cnt += 1

print(cnt)
