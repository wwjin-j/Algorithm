"""
아아ㅏ몰겠다
"""

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def exponential(x, y):
    if y==1:
        return x
    else:
        sub = exponential(x, y//2)
        if y%2==0:
            return (sub*sub)%c
        else:
            return (sub*sub*x)%c

print(exponential(a,b)%c)