"""
250113
2206 벽 부수고 이동하기

n, m row, column 입력받고
n*m map 입력받는다.

0은 이동할 수 있는곳, 1은 이동 못하는 벽
(1, 1) > (n, m)까지 최단경로 이동
벽은 딱 한개 부술 수 있다.
이동할 수 있는 칸은 상하좌우 인접
최단경로 거리 출력
불가능하다면 -1 출력

기본 bfs 에서 벽 부수기 추가
"""
import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    queue = deque([(0, 0, 0)])
    while queue:
        x, y, broken = queue.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][broken]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 0 and visited[nx][ny][broken] == 0:
                    visited[nx][ny][broken] = visited[x][y][broken] + 1
                    queue.append((nx, ny, broken))

                if maps[nx][ny] == 1 and broken == 0 and visited[nx][ny][1] == 0:
                    visited[nx][ny][1] = visited[x][y][broken] + 1
                    queue.append((nx, ny, 1))

    return -1

n, m = map(int, input().split())
maps = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

print(bfs())


