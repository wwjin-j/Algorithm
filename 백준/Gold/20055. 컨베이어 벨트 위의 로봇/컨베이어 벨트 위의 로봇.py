"""
20055
컨베이어 벨트 위의 로봇
"""
import sys
from collections import deque
input = sys.stdin.readline

# 입력 처리
n, k = map(int, input().split())
dq = deque(map(int, input().split()))
r = deque([0] * n)

def rotate():
    dq.rotate(1)
    r.rotate(1)
    if r[n - 1] == 1:
        r[n - 1] = 0

def start():
    if dq[0] > 0 and r[0] == 0:
        r[0] = 1
        dq[0] -= 1

def move():
    for i in range(n - 2, -1, -1):
        if r[i] == 1 and r[i + 1] == 0 and dq[i + 1] > 0:
            r[i], r[i + 1] = 0, 1
            dq[i + 1] -= 1
    if r[n - 1] == 1:
        r[n - 1] = 0

def check_value():
    count = sum(1 for x in dq if x <= 0)
    return count < k

cnt = 0

while True:
    cnt += 1
    rotate()
    move()
    start()
    if not check_value():
        break

print(cnt)