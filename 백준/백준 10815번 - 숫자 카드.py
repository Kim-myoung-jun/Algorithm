import sys
input = sys.stdin.readline

n = int(input())
data1 = list(map(int, input().split()))
m = int(input())
data2 = list(map(int, input().split()))

data1.sort()
def find(target, start, end):
  if start > end:
    return 0  
  mid = (start + end) // 2

  if data1[mid] == target:
    return 1
  elif data1[mid] > target:
    return find(target, start, mid-1)
  else:
    return find(target, mid+1, end)
for i in range(m):
  print(find(data2[i], 0, n-1), end=' ')
