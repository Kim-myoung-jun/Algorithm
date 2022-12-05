import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
data = list(map(int, input().split()))

cnt = abs(100-n)
for i in range(1000001):
    num = str(i)
    for j in range(len(num)):
        if int(num[j]) in data:
            break
        elif j == len(num)-1:
            tmp = abs(n - i) + len(num)
            cnt = min(cnt, tmp)
            
print(cnt)
