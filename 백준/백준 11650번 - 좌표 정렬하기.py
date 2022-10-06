import sys
n = int(sys.stdin.readline())
data = []
for _ in range(n):
    input_data = list(map(int, sys.stdin.readline().split()))
    data.append((input_data[0], input_data[1]))

data.sort(key = lambda b: b[1])
data.sort(key = lambda a: a[0])

for i in data:
    print(i[0], i[1])
