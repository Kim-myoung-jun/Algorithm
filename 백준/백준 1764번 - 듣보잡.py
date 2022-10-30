# https://www.acmicpc.net/problem/1764

# https://wook-2124.tistory.com/476
# https://velog.io/@inyong_pang/Python-List-Tuple-Dictionary-and-Set-%EC%9A%94%EC%95%BD

import sys
n, m = map(int, sys.stdin.readline().split())
a = set()
for _ in range(n):
  a.add(sys.stdin.readline().rstrip())
b = set()
for _ in range(m):
  b.add(sys.stdin.readline().rstrip())

c = sorted(list(a & b))
print(len(c))
for i in c:
  print(i)
