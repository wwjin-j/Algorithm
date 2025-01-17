"""
20057 마법사 상어와 토네이도

N*N 입력받고
토네이도 시전

함수 1) 토네이도 위치 반환
초기 n//2, n//2
(0, -1), (1, 0), (0, 1), (-1, 0)
서 1 남 1
동 2 북 2

서 3 남 3
동 4 북 4
.
.
.
서 n-1 남 n-1
동 n 북 n

서 n


함수 2) 토네이도 모래
"""
import sys
input = sys.stdin.readline

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
dv = [(0, -1), (1, 0), (0, 1), (-1, 0)]
storm = [
    [0, 0, 2, 0, 0],
    [0, 10, 7, 1, 0],
    [5, 0, 0, 0, 0],
    [0, 10, 7, 1, 0],
    [0, 0, 2, 0, 0]]

def rotate_storm(storm, direction):
    """
    스프레드 테이블을 방향에 따라 회전합니다.
    시계 반대 방향으로 회전합니다.
    direction: 0(원본), 1(90도), 2(180도), 3(270도)
    """
    for _ in range(direction):
        storm = [list(row) for row in zip(*storm)][::-1]
    return storm

def spread_sand(r, c, d):
    global maps, N, dv, storm
    sand_out = 0
    sand = maps[r][c]
    maps[r][c] = 0

    total_spread = 0
    dr, dc = dv[d]

    # 현재 방향에 맞게 스프레드 테이블 회전
    rotated_storm = rotate_storm(storm, d)

    for i in range(-2, 3):
        for j in range(-2, 3):
            if rotated_storm[i + 2][j + 2] == 0:
                continue
            nr, nc = r + i, c + j
            spread = (sand * rotated_storm[i + 2][j + 2]) // 100
            if 0 <= nr < N and 0 <= nc < N:
                maps[nr][nc] += spread
            else:
                sand_out += spread
            total_spread += spread

    # 남은 모래(alpha)
    alpha_sand = sand - total_spread
    alpha_r, alpha_c = r + dr, c + dc
    if 0 <= alpha_r < N and 0 <= alpha_c < N:
        maps[alpha_r][alpha_c] += alpha_sand
    else:
        sand_out += alpha_sand

    return sand_out

def tornado():
    r, c = N // 2, N // 2
    direction = 0
    sand_out = 0

    for step in range(1, N):
        for _ in range(2):
            for _ in range(step):
                r, c = r + dv[direction][0], c + dv[direction][1]
                if maps[r][c] == 0:
                    continue
                #print(r, c, direction)
                sand_out += spread_sand(r, c, direction)
            direction = (direction + 1) % 4

    direction = 0
    for _ in range(N - 1):
        r, c = r + dv[direction][0], c + dv[direction][1]
        #print(r, c, direction)
        sand_out += spread_sand(r, c, direction)

    return sand_out

print(tornado())





