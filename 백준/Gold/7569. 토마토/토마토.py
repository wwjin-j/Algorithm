import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

q = deque()
for z in range(h):
    for y in range(n):
        for x in range(m):
            if arr[z][y][x] == 1:
                q.append((z, y, x))

def bfs():
    while q:
        z, y, x = q.popleft()
        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and arr[nz][ny][nx] == 0:
                arr[nz][ny][nx] = arr[z][y][x] + 1
                q.append((nz, ny, nx))

bfs()

result = 0
for box in arr:
    for row in box:
        if 0 in row:
            print(-1)
            exit()
        result = max(result, max(row))

print(result - 1)