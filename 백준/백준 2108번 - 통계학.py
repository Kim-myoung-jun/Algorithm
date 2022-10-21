# https://www.acmicpc.net/problem/2108
import sys
import math
n = int(sys.stdin.readline())
data = []
d2 = [0] * 8001
for _ in range(n):
    k = int(sys.stdin.readline())
    data.append(k)
    d2[k+4000] += 1
data.sort()
print(round(sum(data)/n))
print(data[int(n//2)])

max = max(d2)
count = d2.count(max)
find_second = 0
if count > 1:
    for i in range(len(d2)):
        if max == d2[i]:
            find_second += 1
            if find_second == 2:
                print(i-4000)
                break
else:
    print(d2.index(max)-4000)
print(data[n-1] - data[0])
