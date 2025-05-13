"""
산성, 알카리성
각 용액 특성을 나타내는 정수가 주어진다.
산성 : 1 ~ 10^9
알카리성 : -1 ~ -10^9

혼합용액 특성 : 합, >> 0에 가장 가깝게

0에 가장 가까운 용액을 만드는 세 용액 찾는 프로그램 작성

특성값 정렬되어 입력됨, 두 용액 출력
"""

import sys

n = int(input())
array = list(map(int, input().split()))

array.sort()
minTake = sys.maxsize

for i in range(n - 2):
    start = i + 1
    end = n - 1
    while start < end:
        take = array[i] + array[start] + array[end]
        if abs(take) < minTake:
            minTake = abs(take)
            result = [array[i], array[start], array[end]]
        if take < 0:
            start += 1
        elif take > 0:
            end -= 1
        else:
            break

print(result[0], result[1], result[2])



