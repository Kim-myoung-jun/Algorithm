import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
  lst = list(map(int, input().split()))
  data.append(lst)
  
data.sort(key=lambda x:x[0])
data.sort(key=lambda x:x[1])
end = data[0][1]
cnt = 1
for i in range(1, n):
  if end <= data[i][0]:
    cnt += 1
    end = data[i][1]

print(cnt)

'''
import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
  lst = list(map(int, input().split()))
  data.append(lst)
  
data.sort(key=lambda x:x[0])
data.sort(key=lambda x:x[1])
ans = [[data[0][0], data[0][1]]]

for i in range(1, n):
  if ans[len(ans)-1][1] <= data[i][0]:
    ans.append(data[i])

print(len(ans))
'''
