"""
14658번

n : col
m : row
l : 트램폴린 사이즈(l*l)
k : 별똥별 수
(x, y) * k 가로, 세로 좌표
"""
import sys
input = sys.stdin.readline

n, m, l, k = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(k)]

max_cnt = 0

for i in range(k):
    for j in range(k):
        cnt = 0
        for x in range(k):
            if info[i][0] <= info[x][0] <= info[i][0]+l and info[j][1] <= info[x][1] <= info[j][1] + l:
                cnt += 1
        max_cnt = max(max_cnt, cnt)

print(k-max_cnt)