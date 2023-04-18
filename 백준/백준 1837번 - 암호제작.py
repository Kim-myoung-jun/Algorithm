import sys
from collections import deque
input = sys.stdin.readline
pq, k = map(int ,input().split())
base = k-1
isPrime = [1]*(base+1)
isPrime[0] = isPrime[1] = 0
for i in range(base+1):
    if isPrime[i]:
        for j in range(i*i, base+1, i):
            isPrime[j] = 0
            
prime = []
for i in range(2, base+1):
    if isPrime[i]:
        prime.append(i)
        
flag = True
for i in prime:
    if pq % i == 0:
        flag = False
        print('BAD', i)
        break
if flag:
    print('GOOD')
