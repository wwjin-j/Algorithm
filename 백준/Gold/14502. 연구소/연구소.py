"""
14502 연구소

NxM  직사각형
0 빈칸
1 벽
2 바이러스(상하좌우 퍼짐)

벽은 3개 세울 수 있다 꼭 3개 세운다

안전 영역 크기의 최댓값

함수들
1. 바이러스 퍼짐
2. 안전영역 구하기
3. 벽 3개 세우기

벽 세우고 >> 바이러스 퍼트리고 >> 안전지대 카운트 해서 >> max 갱신
"""
import sys
from itertools import combinations
from collections import deque
import copy

input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 바이러스 spread(전형적인 bfs)
def virus(tmp_map):
    queue = deque()
    for i in range(n):
        for j in range(m):
            if tmp_map[i][j] == 2:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and tmp_map[nx][ny] == 0:
                tmp_map[nx][ny] = 2
                queue.append((nx, ny))

# tmp map에서 0 개수 카운트
def safe(tmp_map):
    return sum(row.count(0) for row in tmp_map)

empty_spaces = [(i, j) for i in range(n) for j in range(m) if maps[i][j] == 0]
max_safe_area = 0

# empty space 에서 3개 선택
for walls in combinations(empty_spaces, 3):
    tmp_map = copy.deepcopy(maps) # 원본 카피 이후
    for x, y in walls:
        tmp_map[x][y] = 1 #추가된 벽 추가
    virus(tmp_map) # 바이러스 퍼트리기
    max_safe_area = max(max_safe_area, safe(tmp_map))

print(max_safe_area)


