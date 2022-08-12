x = []
y = []
for i in range(3):
  a, b = map(int, input().split())
  x.append(a)
  y.append(b)

x.sort()
y.sort()

q = x[0]-x[1]+x[2]
w = y[0]-y[1]+y[2]

print(q, w)
'''
#다른 
data = []
for i in range(3):
  data.append(list(map(int, input().split())))

a, b = 0, 0
if data[0][0] == data[1][0]:
  a = data[2][0]
elif data[0][0] == data[2][0]:
  a = data[1][0]
else:
  a = data[0][0]

if data[0][1] == data[1][1]:
  b = data[2][1]
elif data[0][1] == data[2][1]:
  b = data[1][1]
else:
  b = data[0][1]

print(a, b)

'''
