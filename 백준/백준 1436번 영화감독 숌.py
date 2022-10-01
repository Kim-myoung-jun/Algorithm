import sys
n = int(sys.stdin.readline())

cnt = 666
while n != 0:
    if "666" in str(cnt):
        n -= 1
        if n == 0:
            break
    cnt += 1
print(cnt)
