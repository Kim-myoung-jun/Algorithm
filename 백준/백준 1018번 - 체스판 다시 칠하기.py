n, m = map(int, input().split())
data = []

for i in range(n):
    data.append(input())
    
cnt = 9999999
tmp = 0
for i in range(n-7):
    for j in range(m-7):
        case1 = 0
        case2 = 0
        for q in range(i, i+8):
            for w in range(j, j+8):
                if (q+w) % 2 == 0:
                    if data[q][w] != 'B':
                        case1 += 1
                    if data[q][w] != 'W':
                        case2 += 1
                else:
                    if data[q][w] != 'W':
                        case1 += 1
                    if data[q][w] != 'B':
                        case2 += 1
                        
        tmp = min(case1, case2)
        if cnt > tmp:
            cnt = tmp
            
print(cnt)
