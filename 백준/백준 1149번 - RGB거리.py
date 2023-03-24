import sys
input = sys.stdin.readline
n = int(input())
house = [ [0] * 3 for _ in range(1001) ]

for i in range(1, n+1):
    r, g, b = map(int ,input().split())
    house[i][0] = min(house[i-1][1], house[i-1][2]) + r
    house[i][1] = min(house[i-1][0], house[i-1][2]) + g
    house[i][2] = min(house[i-1][0], house[i-1][1]) + b
    
print(min(house[n]))
