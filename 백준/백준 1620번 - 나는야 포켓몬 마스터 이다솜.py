# https://www.acmicpc.net/problem/1620

import sys
n, m = map(int, sys.stdin.readline().split())
s = {}
s2 = {}
for i in range(n):
    a = sys.stdin.readline().rstrip()
    s[i+1] = a
    s2[a] = i+1
    

for i in range(m):
    k = sys.stdin.readline().rstrip()
    if k.isdecimal():
        print(s.get(int(k)))
    else:
        print(s2.get(k))
