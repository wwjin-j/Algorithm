"""
250115
15683 감시

map에서 해당 사각지대의 최소값을 구하는 문제

cctv 는 모두 수직으로 감시, 회전 가능

1번 cctv 한 방향
2번 cctv 두 방향(반대)
3번 cctv 두 방향(수직)
4번 cctv 세 방향
5번 cctv 네 방향
"""
import sys
from copy import deepcopy
input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
cctv = []
directions = {
    1: [[0], [1], [2], [3]],  # 한 방향
    2: [[0, 1], [2, 3]],      # 반대 방향
    3: [[0, 2], [0, 3], [1, 2], [1, 3]],  # 직각 방향
    4: [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],  # 세 방향
    5: [[0, 1, 2, 3]]  # 네 방향
}

# CCTV 위치 저장
for i in range(n):
    for j in range(m):
        if 1 <= maps[i][j] <= 5:
            cctv.append((i, j, maps[i][j]))

# 방향 이동
d = [
    (0, 1),  # 동
    (0, -1), # 서
    (1, 0),  # 남
    (-1, 0)  # 북
]

# 감시 영역 표시
def monitor(temp_map, x, y, dirs):
    for dir in dirs:
        nx, ny = x, y
        while True:
            nx += d[dir][0]
            ny += d[dir][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or temp_map[nx][ny] == 6:
                break  # 맵을 벗어나거나 벽을 만나면 종료
            if temp_map[nx][ny] == 0:
                temp_map[nx][ny] = -1  # 감시 표시

# 사각지대 계산
def count_blind_spots(temp_map):
    return sum(row.count(0) for row in temp_map)

# DFS를 이용한 모든 경우 탐색
def dfs(depth, temp_map):
    global min_blind_spots
    if depth == len(cctv):  # 모든 CCTV 처리 완료
        min_blind_spots = min(min_blind_spots, count_blind_spots(temp_map))
        return

    x, y, cctv_type = cctv[depth]
    for dirs in directions[cctv_type]:
        new_map = deepcopy(temp_map)
        monitor(new_map, x, y, dirs)  # 현재 CCTV 감시 영역 표시
        dfs(depth + 1, new_map)  # 다음 CCTV로 진행

# 초기화
min_blind_spots = float('inf')
dfs(0, maps)
print(min_blind_spots)


