"""
산성, 알카리성
각 용액 특성을 나타내는 정수가 주어진다.
산성 : 1 ~ 10^9
알카리성 : -1 ~ -10^9

혼합용액 특성 : 합, >> 0에 가장 가깝게

0에 가장 가까운 용액을 만드는 두 용액 찾는 프로그램 작성

특성값 정렬되어 입력됨, 두 용액 출력
"""

import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

idx_1, idx_2 = 0, n - 1
ans = float('inf')
ans_idx_1, ans_idx_2 = idx_1, idx_2

while idx_1 < idx_2:
    tmp = li[idx_1] + li[idx_2]
    if abs(tmp) < ans:
        ans = abs(tmp)
        ans_idx_1, ans_idx_2 = idx_1, idx_2
        if ans == 0:
            break
    if tmp < 0:
        idx_1 += 1
    else:
        idx_2 -= 1

print(li[ans_idx_1], li[ans_idx_2])