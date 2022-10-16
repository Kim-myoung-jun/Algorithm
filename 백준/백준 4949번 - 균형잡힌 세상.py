import sys
while True:
    stack = []
    s = input()
    flag = "yes"
    if s[0] == ".":
        break
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')' or i == ']':
            if len(stack) == 0:
                flag = "no"
                break
            else:
                check = stack.pop()
                if i == ')' and check != '(':
                    flag = "no"
                    break
                elif i == ']' and check != '[':
                    flag = "no"
                    break
    if len(stack) > 0:
        print("no")
    else:
        print(flag)
