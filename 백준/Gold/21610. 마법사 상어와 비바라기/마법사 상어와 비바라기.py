"""
250117
21610 마법사 상어와 비바라기

N*N 격자에서 비바라기를 연습한다
r, c >> 좌표
li[r][c] >> 물의 양
(1, 1) ~ (N, N)

비바라기 시전~
(N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생긴다

이동명령 (d, s) > 방향, 거리
←, ↖, ↑, ↗, →, ↘, ↓, ↙

1. d방향 s만큼 이동
2. 비 내려 해당 칸 바구니 저장된 물의 양 1 증가
3. 구름 소멸
4. 물복사버그 시전
    1) 대각선 방향 거리 1인 칸 물이있는 바구니 수 만큼 물양 증가
    2) 원래 프레임 기준 original n*n
5. 물의 양이 2 이상이면 구름생김, 물의 양 2 줄어듬

함수정리
1. 구름 이동하는 함수 __(1)
2. 비 내리고 구름 소멸하는 함수 __(2), (3)
3. 물복사 버그 함수(4)
4. 구름생성 함수


"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
commands = [list(map(int, input().split())) for _ in range(M)]

dv = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

# 초기 구름 위치
clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

def move(clouds, d, s):
    new_clouds = []
    for r, c in clouds:
        nr = (r + dv[d][0] * s) % N
        nc = (c + dv[d][1] * s) % N
        new_clouds.append((nr, nc))
    return new_clouds

def rain(clouds):
    for r, c in clouds:
        maps[r][c] += 1
    return set(clouds)

def bug(clouds):
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for r, c in clouds:
        count = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and maps[nr][nc] > 0:
                count += 1
        maps[r][c] += count

def create(previous_clouds):
    new_clouds = []
    for r in range(N):
        for c in range(N):
            if maps[r][c] >= 2 and (r, c) not in previous_clouds:
                new_clouds.append((r, c))
                maps[r][c] -= 2
    return new_clouds

for d, s in commands:
    clouds = move(clouds, d - 1, s)
    previous_clouds = rain(clouds)
    bug(previous_clouds)
    clouds = create(previous_clouds)

result = sum(sum(row) for row in maps)
print(result)