# https://www.acmicpc.net/problem/1003

import sys
dp = [[0, 0] for i in range(41)]
dp[0] = [1, 0]
dp[1] = [0, 1]

def fibo(q):
    if q == 0 or q == 1:
        return
    for i in range(2, q+1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]
t = int(sys.stdin.readline())
for _ in range(t):
  q = int(sys.stdin.readline())
  fibo(q)
  print(dp[q][0], dp[q][1])
