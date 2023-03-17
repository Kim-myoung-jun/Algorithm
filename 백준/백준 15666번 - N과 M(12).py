import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(str, input().split()))
arr.sort(key=int)
stack = []

def dfs(index):
    if index == m:
        print(' '.join(stack))
        return
    tmp = -1
    com = -1
    if len(stack) > 0:
        com = int(stack[len(stack)-1])
    for i in range(n):
        if int(arr[i]) > int(tmp) and int(arr[i]) >= com:
            stack.append(arr[i])
            dfs(index+1)
            tmp = stack.pop()
dfs(0)
