while True:
  s = input()
  if s == "0":
    break
  ls = list(s)
  rs = reversed(ls)
  if s == ''.join(rs):
    print("yes")
  else:
    print("no")
