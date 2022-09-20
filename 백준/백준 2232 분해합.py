n = input()

min_m = int(n)-len(n)*9
check = 0
if min_m <= 0:
  min_m = 0
for i in range(min_m, int(n)):
  s_i = str(i)
  data = []
  for j in s_i:
    data.append(int(j))
  data.append(i)
  if sum(data) == int(n):
    check = 1
    break;
if check == 1:
  print(data[len(data)-1])
else:
  print(0)
