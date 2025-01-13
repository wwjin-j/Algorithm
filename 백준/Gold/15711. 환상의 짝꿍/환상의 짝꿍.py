import sys
from math import sqrt
input = sys.stdin.readline

MAX = 2000001
prime = [0] * MAX
prime[1] = 1

for i in range(2, int(sqrt(MAX)) + 1):
    if prime[i] == 0:
        for j in range(i + i, MAX, i):
            prime[j] = 1

prime_list = [i for i in range(2, MAX) if prime[i] == 0]

def is_prime(n):
    for p in prime_list:
        if p * p > n:
            break
        if n % p == 0:
            return 0
    return 1

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    total = a + b

    if total < 4:
        print("NO")
    elif total % 2 == 0:
        print("YES")
    else:
        total -= 2
        if is_prime(total):
            print("YES")
        else:
            print("NO")