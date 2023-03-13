import sys
input = sys.stdin.readline
n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
stack = []
visited = []
visited2 = [ False for _ in range(n)]
def dfs(now, index): #현재 위치, 스택의 길이
    global visited
    if index == m:
        if ' '.join(stack) not in visited: #정답으로 출력되지 않은 경우
            print(' '.join(stack))
            visited.append(' '.join(stack)) #정답 리스트에 추가
            return
        else:
            return
    for i in range(n):
        if len(stack) != 0 and now == i: #같은 자리의 중복 방지
            continue
        if not visited2[i]:
            stack.append(str(arr[i]))
            visited2[i] = True #자리 체크
            dfs(i, index+1)
            stack.pop()
            visited2[i] = False
                
dfs(0, 0)

'''
#더 좋은 풀이
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = input().split()
arr.sort(key=int) #key=int 없으면 값이 달라짐
stack = []
visited = [0] * n

def dfs(index):
    if index == m:
        print(' '.join(stack))
        return
    now = -1 #자연수이므로 -1로 초기화
    for i in range(n):
        if visited[i] or now == arr[i]: #방문했거나, 값이 같다면 넘기기
            continue
        visited[i] = 1
        stack.append(arr[i])
        dfs(index+1)
        visited[i] = 0
        now = stack.pop() #가장 마지막 값을 빼면서 결과값의 중복 체크

dfs(0)
'''
