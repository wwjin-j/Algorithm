import sys

n, s = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

start, end = 0, 0
current_sum = 0
min_length = float('inf')

while end < n:
    current_sum += li[end]
    end += 1

    while current_sum >= s:
        min_length = min(min_length, end - start)
        current_sum -= li[start]
        start += 1

print(min_length if min_length != float('inf') else 0)