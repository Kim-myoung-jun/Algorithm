# https://www.acmicpc.net/problem/1012

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())

def find(x, y):
    if x < 0 or y < 0 or x == m or y == n:
        return False
    
    if data[x][y] == 1:
        data[x][y] = 2
        find(x-1, y)
        find(x, y-1)
        find(x+1, y)
        find(x, y+1)
        return True
    return False
    

for _ in range(t):
    m, n, k = map(int, input().split())
    data = [ [0] * n for i in range(m) ]
    cnt = 0
    for _ in range(k):
        x, y = map(int, input().split())
        data[x][y] = 1
    for i in range(m):
        for j in range(n):
            if find(i, j) == True:
                cnt += 1
    print(cnt)
