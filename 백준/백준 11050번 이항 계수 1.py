import math
n, k = map(int, input().split())
r = int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))
print(r)
