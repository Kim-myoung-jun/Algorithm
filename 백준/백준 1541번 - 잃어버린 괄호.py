s = input()
num = []
oper = []
input_num = ""
for i in range(len(s)):
  if ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9'):
    input_num += s[i]
  else:
    num.append(int(input_num))
    input_num = ""
    oper.append(s[i])
num.append(int(input_num))

#print(num)
#print(oper)

for i in range(len(oper)):
  if oper[i] == '+':
    #print(type(num[i]))
    if type(num[i]) is int:
      num[i] = num[i]+num[i+1]
      num[i+1] = [num[i], i]
      oper[i] = 'x'
    else:
      num[num[i][1]] = num[i][0] + num[i+1]
      num[i+1] = [num[num[i][1]], num[i][1]]
      oper[i] = 'x'
sum = 0
check = False
for i in range(len(num)):
  if type(num[i]) is int:
    if check == False:
      sum = num[i]
      check = True
    else:
      sum -= num[i]

print(sum)

'''
s = input()
arr = s.split("-")
total = 0
for i in range(len(arr)):
  sum = 0;
  if "+" in arr[i]:
    arr_sum = list(map(int, arr[i].split("+")))
    for j in arr_sum:
      sum += j
  else:
    sum = int(arr[i])

  if i==0:
    total = sum
  else:
    total -= sum

print(total)
'''