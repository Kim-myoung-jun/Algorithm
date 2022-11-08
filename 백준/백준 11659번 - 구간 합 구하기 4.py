# https://www.acmicpc.net/problem/11659

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
sum = 0
for i in range(n):
    sum += data[i]
    data[i] = sum
for _ in range(m):
    i, j = map(int, input().split())
    if i == 1:
        print(data[j-1])
    else:
        print(data[j-1] - data[i-2])
