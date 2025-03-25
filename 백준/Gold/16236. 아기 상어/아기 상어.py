"""
아기상어 문제

N*N 공간 물고기 M 마리, 아기상어 1마리 있다.

아기상어 초기 크기 : 2
아기상어는 자신보다 큰 물고기 있는 칸 못지나감
아기상어는 자신보다 작은 물고기만 먹을 수 있다.

크기가 같은 물고기는? 지나갈 수 있고 먹지는 못함

먹을 수 있는 물고기들 중 가장 가까운 곳으로 간다.
같은 거리일 경우, 가장 위, 가장 왼쪽 순서로 우선순위

자신의 크기와 같은 수의 물고기 먹으면 크기가 늘어난다.
"""
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]

size = 2
time = 0
cnt = 0
dv = [(-1, 0), (0, -1), (0, 1), (1, 0)]

for i in range(N):
    for j in range(N):
        if maps[i][j] == 9:
            x, y = i, j
            maps[i][j] = 0

def bfs(x, y):
    visited = [[-1]*N for _ in range(N)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    fishes = []

    while q:
        x, y = q.popleft()
        for dx, dy in dv:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == -1 and maps[nx][ny] <= size:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                    if 1 <= maps[nx][ny] < size:
                        fishes.append((visited[nx][ny], nx, ny))

    if not fishes:
        return None
    fishes.sort()
    return fishes[0][1], fishes[0][2], fishes[0][0]

while True:
    result = bfs(x, y)
    if result is None:
        break
    nx, ny, dist = result
    time += dist
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0
    maps[nx][ny] = 0
    x, y = nx, ny

print(time)