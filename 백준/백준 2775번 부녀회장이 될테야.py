T = int(input())
for _ in range(T):
  k = int(input())
  n = int(input())
  data = [[0] * n for _ in range(k+1)]
  
  for i in range(k+1):
    for j in range(n):
      if i == 0:
        data[i][j] = j+1
      else:
        for q in range(j+1):
          data[i][j] += data[i-1][q]
  #print(data)
  print(data[k][n-1])
