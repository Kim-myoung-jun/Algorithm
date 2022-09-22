n, m = map(int, input().split())

data = list(map(int, input().split()))
sum = 0
for i in range(len(data)-2):
    for j in range(i+1, len(data)-1):
        for k in range(j+1, len(data)):
            tmp = data[i]+data[j]+data[k]
            if sum < tmp and tmp <= m:
                sum = tmp
            if(sum == m):
                break
print(sum)
