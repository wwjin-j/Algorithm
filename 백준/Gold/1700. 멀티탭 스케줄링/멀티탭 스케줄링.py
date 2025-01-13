"""
250113
1700 멀티탭 스케줄링

n, k
li
n : 멀티탭 구멍의 개수
k : 사용횟수
li : 사용순서
"""
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
li = deque(map(int, input().split()))
mt = deque()

cnt = 0

def choose(mt, li):
    farthest_idx = -1
    remove_device = -1

    for device in mt:
        try:
            next_use = li.index(device)
        except ValueError:
            return device

        if next_use > farthest_idx:
            farthest_idx = next_use
            remove_device = device

    return remove_device

for _ in range(k):
    cur = li.popleft()

    if cur in mt:
        continue
    if len(mt) < n:
        mt.append(cur)
    else:
        device_to_remove = choose(mt, li)
        mt.remove(device_to_remove)
        mt.append(cur)
        cnt += 1

print(cnt)
