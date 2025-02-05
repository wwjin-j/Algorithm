import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
maps = [list(map(int, input().rstrip())) for _ in range(N)]

apt = []

dv = [(0, -1), (0, 1), (1, 0), (-1, 0)]

def bfs(row, col):
    q = deque()
    q.append((row, col))
    maps[row][col] = 0
    cnt = 1
    while q:
        x, y = q.popleft()
        maps[x][y] = 0
        for dx, dy in dv:
            nx, ny = x+dx, y+dy
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if maps[nx][ny]==1:
                maps[nx][ny]=0
                q.append((nx, ny))
                cnt += 1
    return cnt

for i in range(N):
    for j in range(N):
        if maps[i][j]==1:
            cnt = bfs(i, j)
            apt.append(cnt)
apt.sort()

print(len(apt))
for x in apt:
    print(x)


