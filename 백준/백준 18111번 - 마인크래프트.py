# https://www.acmicpc.net/problem/18111

import sys
import math
n, m, b = map(int, sys.stdin.readline().split())
data = []
for _ in range(n):
    data += list(map(int, sys.stdin.readline().split()))
    
min_h = min(data)
max_h = max(data)

result_sec = 99999999
result_h = 0
for h in range(min_h, max_h+1):
    tmp_sec = 0
    tmp_h = b
    for i in range((n*m)):
        if data[i] > h:
            tmp_sec += (data[i] - h) * 2
            tmp_h += (data[i] - h)
        else: #data[i] < h
            tmp_sec += (h - data[i])
            tmp_h -= (h - data[i])
    if tmp_h >= 0:
        if result_sec >= tmp_sec:
            result_sec = tmp_sec
            result_h = h
            
print(result_sec, result_h)
