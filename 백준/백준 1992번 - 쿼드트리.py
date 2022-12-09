import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

n = int(input())
data = []
s = ""
for _ in range(n):
    data.append(list(map(int, input().strip())))
    
def check(a, b, size):
    point = data[a][b]
    for i in range(a, a+size):
        for j in range(b, b+size):
            if point != data[i][j]:
                return False
    return True

def devide(a, b, size):
    global s
    if check(a, b, size) == True:
        
        if data[a][b] == 0:
            s+="0"
        else:
            s+="1"
        
        return
    else:
        size //= 2
        s+="("
        devide(a, b, size)
        devide(a, b+size, size)
        devide(a+size, b, size)
        devide(a+size, b+size, size)
        s+=")"

devide(0, 0, n)
print(s)
