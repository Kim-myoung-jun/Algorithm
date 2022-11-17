# https://www.acmicpc.net/problem/2630

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    lst = list(map(int, input().split()))
    data.append(lst)

blue = 0
white = 0

def checkColor(row, col, size):
    fix = data[row][col]
    for i in range(row, row+size):
        for j in range(col, col+size):
            if fix != data[i][j]:
                return False
    return True
    
def devide(row, col, size):
    global white
    global blue
    if checkColor(row, col, size):
        if(data[row][col] == 0):
            white+=1
        else:
            blue+=1
        return
    
    size //=2
    devide(row, col, size)
    devide(row+size, col, size)
    devide(row, col+size, size)
    devide(row+size, col+size, size)
        

devide(0, 0, n)
print(white)
print(blue)
