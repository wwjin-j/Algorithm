"""
250109
7576 토마토 문제
(m, n) 상자의 가로, 세로
row : n
col : m
n 줄에 걸쳐 상자 토마토 받아옴
1 익은 토마토
0 안 익은 토마토
-1 토마토 없음

토마토는 상하좌우 인접한 4개의 토마토 영향을 받아 익는다
토마토가 모두 익는 최소일수 구하기
안익은 것 붙어있으면 하루걸려서 익은놈이 익혀버림

출력
0 : 첨부터 모두 익었을때
-1 : 못익는 토마토가 있으면
result
"""
import sys
from _collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
"""
n : row
m : column
arr : tomato basket
"""
arr = [list(map(int, input().split())) for _ in range(n)]
time = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

q = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j))

def bfs():
    while q:
        row, col = q.popleft()
        for i in range(4):
            n_row = row+dx[i]
            n_col = col+dy[i]
            if 0<=n_row<n and 0<=n_col<m and arr[n_row][n_col]==0:
                arr[n_row][n_col] = arr[row][col]+1
                q.append((n_row, n_col))

bfs()

flag = False
for row in arr:
    for x in row:
        if x == 0:
            time = 0
            flag = True
        if flag:
            break
    if flag:
        break
    else:
        time = max(time, max(row))

print(time-1)
