import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())

def foo(b):
    if b == 1:
        return a % c
    else:
        x = foo(b//2)
        if b % 2 == 0:
            return x*x%c
        else:
            return x*x*a%c
    
print(foo(b))
