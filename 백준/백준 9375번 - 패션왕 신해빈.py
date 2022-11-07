# https://www.acmicpc.net/problem/9375

# ref
# https://hongcoding.tistory.com/60
# https://pacific-ocean.tistory.com/229
# https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-9375-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%8C%A8%EC%85%98%EC%99%95-%EC%8B%A0%ED%95%B4%EB%B9%88-%EC%8B%A4%EB%B2%843-%EC%A1%B0%ED%95%A9%EB%A1%A0

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    data = {}
    for _ in range(n):
        w = list(input().split())
        if w[1] in data:
            data[w[1]].append(w[0])
        else:
            data[w[1]] = [w[0]]
    
    cnt = 1
    for i in data:
        cnt *= len(data[i]) + 1
        
    print(cnt-1)
