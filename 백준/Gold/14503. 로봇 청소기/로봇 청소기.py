"""
250114
24503 로봇청소기

청소기 방향이 있다(동서남북)

청소기 작동 규칙
1. 지금 칸 아직이면 현재 칸 청소
2. 현재 칸 주변 4칸 중 청소 안된 빈 칸 없으면?
    1) 방향 유지한대로 한칸 빠꾸할 수 있다면 한칸빠꾸 후 1번
    2) 한칸 빠꾸하지 못하면(벽) 작동 멈춤
3. 현재 4칸 중 빈칸 있으면?
    1) 반시계 90도 회전
    2) 방향 기준 앞쪽칸 빈칸이면? 한 칸 전진
    3) 1번으로 이동

n, m 입력(row, column)
r, c, d 청소기 초기상태
maps 입력
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

# 동서남북 방향 정의 (북, 동, 남, 서)
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 위치가 유효한지 확인
def position(x, y):
    return 0 <= x < n and 0 <= y < m

# 현재 위치 주변에 청소할 빈 칸이 있는지 확인
def check(x, y):
    for a, b in direction:
        nx, ny = x + a, y + b
        if position(nx, ny) and maps[nx][ny] == 0:
            return True
    return False

# 반시계 방향으로 90도 회전
def rotate(x):
    return (x - 1) % 4

# 로봇 청소기 작동 함수
def robot(x, y, d):
    cnt = 0  # 청소한 칸 개수
    while True:
        # 1. 현재 칸 청소
        if maps[x][y] == 0:
            cnt += 1
            maps[x][y] = -1  # 청소 완료 표시

        # 2. 주변 4칸 중 청소할 곳 확인
        if check(x, y):
            # 2-1. 반시계 회전
            d = rotate(d)
            # 2-2. 앞칸이 청소되지 않은 빈 칸이면 전진
            nx, ny = x + direction[d][0], y + direction[d][1]
            if position(nx, ny) and maps[nx][ny] == 0:
                x, y = nx, ny
        else:
            # 3. 4칸 모두 청소되었거나 벽인 경우
            # 뒤로 이동
            bx, by = x - direction[d][0], y - direction[d][1]
            if position(bx, by) and maps[bx][by] != 1:  # 뒤로 갈 수 있으면
                x, y = bx, by
            else:
                # 3-1. 뒤가 벽이면 작동 종료
                return cnt

# 로봇 청소기 작동 시작
print(robot(r, c, d))