"""
250113
1941 소문난 칠공주
5*5 맵 받아서 7공주 결성 경우의 수 출력

7공주 조건
1. 7명 구성
2. 7명끼리 가로 혹은 세로로 인접
3. 이다솜파 4명 이상
"""
import sys
from collections import deque
input = sys.stdin.readline

maps = [list(map(str, input().strip())) for _ in range(5)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

cnt = 0
princess = []

def bfs(princess):
    queue = deque([princess[0]])
    visited = {princess[0]}
    som_count = 0
    for x, y in princess:
        if maps[x][y] == 'S':
            som_count += 1
    if som_count < 4:
        return False
    connected_count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (nx, ny) in princess and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
                connected_count += 1
    return connected_count == 7

def dfs(depth):
    global cnt
    if len(princess)==7:
        if bfs(princess):
            cnt += 1
        return
    for i in range(depth, 25):
        x, y = i//5, i%5
        princess.append((x, y))
        dfs(i+1)
        princess.pop()
dfs(0)
print(cnt)