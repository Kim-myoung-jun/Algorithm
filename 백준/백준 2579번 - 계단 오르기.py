# https://www.acmicpc.net/problem/2579

import sys
input = sys.stdin.readline

n = int(input())
step = [0] * 300
for i in range(n):
    step[i] = int(input())

d = [0] * 300
d[0] = step[0]
d[1] = step[0] + step[1]
d[2] = max(step[0] + step[2], step[1] + step[2])

if n > 2:
    for i in range(3, n):
        d[i] = max(step[i] + d[i-2], step[i] + step[i-1] + d[i-3])
print(d[n-1])
