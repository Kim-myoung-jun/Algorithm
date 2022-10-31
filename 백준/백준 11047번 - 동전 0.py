# https://www.acmicpc.net/problem/11047

import sys
n, k = map(int, sys.stdin.readline().split())

a = []
for _ in range(n):
    a.append(int(sys.stdin.readline()))
    
a.sort(reverse=True)
cnt = 0
for i in a:
    tmp = 0
    if (k // i) > 0:
        tmp = k // i
        k = k - (i * tmp)
        cnt += tmp
    if k == 0:
        break
print(cnt)
