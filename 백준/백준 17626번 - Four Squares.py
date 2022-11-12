# https://www.acmicpc.net/problem/17626

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 50001
dp[1] = 1
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    j = 1
    while j*j <= i:
        tmp = dp[i - (j*j)] + 1
        dp[i] = min(dp[i], tmp)
        j += 1
        
print(dp[n])
