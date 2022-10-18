# https://loosie.tistory.com/m/267
# https://www.acmicpc.net/problem/1929
import sys
m, n = map(int, sys.stdin.readline().split())

isPrime = [1] * (n+1)
isPrime[0] = isPrime[1] = 0

for i in range(2, n+1):
  if isPrime[i]:
    for j in range(i*i, n+1, i):
      isPrime[j] = 0

for i in range(m, n+1):
  if isPrime[i]:
    print(i, end=' ')
