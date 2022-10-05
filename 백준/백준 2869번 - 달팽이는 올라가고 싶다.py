import sys
import math
a, b, v = map(int, sys.stdin.readline().split())
cnt = (v-b) / (a-b)
print(math.ceil(cnt))
