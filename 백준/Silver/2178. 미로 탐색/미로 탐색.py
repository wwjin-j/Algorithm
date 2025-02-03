import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, input().strip())) for _ in range(N)]

dv = [(0, -1), (0, 1), (1, 0), (-1, 0)]

def bfs():
    q = deque()
    q.append((0, 0))
    visited = [[-1] * M for _ in range(N)]
    visited[0][0] = 1

    while q:
        x, y = q.popleft()

        if x == N - 1 and y == M - 1:
            return visited[x][y]

        for dx, dy in dv:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M:
                if maps[nx][ny] == 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

    return -1 

print(bfs())