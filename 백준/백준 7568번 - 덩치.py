import sys
n = int(sys.stdin.readline())
data = []
result = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    data.append((x, y))

for i in range(n):
    cnt = 1
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            cnt += 1
    result.append(cnt)

for i in result:
    print(i, end=' ')
