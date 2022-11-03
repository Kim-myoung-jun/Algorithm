# https://www.acmicpc.net/problem/1463

# 이코테 버전
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 1000001

for i in range(2, n+1):
  dp[i] = dp[i-1] + 1
  if i % 2 == 0:
    dp[i] = min(dp[i], dp[i//2]+1)
  if i % 3 == 0:
    dp[i] = min(dp[i], dp[i//3]+1)
    
print(dp[n])

# 내가 직접 작성한 코드
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 1000001

dp[2] = 1
dp[3] = 1
for i in range(4, n+1):
  a = 987654321
  b = 987654321
  c = 987654321
  if i % 3 == 0:
    a = dp[i//3] + 1
  if i % 2 == 0:
    b = dp[i//2] + 1
  c = dp[i-1] + 1
  
  dp[i] = min(a, b, c)
print(dp[n])
