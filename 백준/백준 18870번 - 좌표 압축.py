import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
set_data = set(data)
sort_data = list(set_data)
sort_data.sort()

cnt_data = {}
for i in range(len(sort_data)):
  cnt_data[sort_data[i]] = i

for i in range(len(data)):
  print(cnt_data[data[i]], end=' ')
