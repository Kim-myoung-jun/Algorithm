import sys
input = sys.stdin.readline

p, n = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
cnt = 0
while p < 200 and cnt < n:
  p += data[cnt]
  cnt += 1
print(cnt)
