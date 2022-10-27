# https://www.acmicpc.net/problem/11723
import sys
m = int(sys.stdin.readline())
s = 0b0
for _ in range(m):
    o = sys.stdin.readline().rstrip().split()
    if o[0] == "all":
        s = 0b111111111111111111111
    elif o[0] == "empty":
        s = 0b0
    else:
        order = o[0]
        x = int(o[1])
        if order == "add":
            s = s | (0b1 << x)
        elif order == "remove":
            s = s & ~(0b1 << x)
        elif order == "check":
            if s & (0b1 << x):
                print(1)
            else:
                print(0)
        #elif order == "toggle":
        else:
            s = s ^ (0b1 << x)
            
  # ref - https://coarmok.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%ACpython-%EB%B0%B1%EC%A4%80-11723%EB%B2%88-%EB%B9%84%ED%8A%B8%EB%A7%88%EC%8A%A4%ED%82%B9?category=910483
# ref - https://velog.io/@1998yuki0331/Python-%EB%B9%84%ED%8A%B8-%EB%A7%88%EC%8A%A4%ED%82%B9-%EC%A0%95%EB%A6%AC
