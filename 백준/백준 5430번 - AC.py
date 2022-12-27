import sys
input = sys.stdin.readline

t= int(input())
for _ in range(t):
  p = input().strip()
  n = int(input())
  s = input().strip()
  s = s[1:len(s)-1] #끝에 [ ] 제거
  if len(s) > 0:
    data = s.split(",")
  else:
    data = []
  flag = 0 # 0 - 정, 1 - 역, 2 - 에러
  for i in p:
    if i == 'R':
      if flag == 0:
        flag = 1
      else:
        flag = 0
    else:
      if len(data) > 0:
        if flag == 0:
          del data[0] #정방향 일때 맨 앞 제거
        else:
          del data[-1] # 역방향 일때 맨 뒤 제거
      else:
        flag = 2 # 데이터가 비어있으면 에러 플래그
        break
  if flag == 2:
    print("error")
    continue
  elif flag == 1:
    data.reverse() # 역방향이면 전환

  print("[", end='')
  for i in range(len(data)):
    print(data[i], end='')
    if i < len(data)-1:
      print(",", end='')
  print("]")
