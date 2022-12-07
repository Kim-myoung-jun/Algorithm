import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

def check(x, y, size):
    point = data[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if point != data[i][j]:
                return False
    return True

def recur(x, y, size):
    if check(x, y, size) == True:
        global m_1
        global zero
        global p_1
        if data[x][y] == -1:
            m_1 += 1
        elif data[x][y] == 0:
            zero += 1
        else:
            p_1 += 1
    else:
        size //= 3
        recur(x, y, size)
        recur(x, y+size, size)
        recur(x, y+size+size, size)
        recur(x+size, y, size)
        recur(x+size, y+size, size)
        recur(x+size, y+size+size, size)
        recur(x+size+size, y, size)
        recur(x+size+size, y+size, size)
        recur(x+size+size, y+size+size, size)

n = int(input())
data = [ []*n for _ in range(n)]
for i in range(n):
    lst = list(map(int, input().split()))
    data[i] = lst
    
m_1 = 0
p_1 = 0
zero = 0
recur(0, 0, n)
print(m_1)
print(zero)
print(p_1)
