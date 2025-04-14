"""
주사위 굴리기 14499

크기 N*M 지도
각 칸은 0으로 초기화

주사위 굴려서 이동했을 때,
1. 칸의 수 == 0 -> 주사위 바닥 수 칸에 복사
2. 칸의 수 != 0 -> 칸의 수 주사위 바닥에 복사, 칸의 수는 0으로 바뀜

입력
N, M, X, Y, K 지도 크기, 주사위 초기 좌표, 명령 개수

명령 1234 동서북남
   1
3  0  2
   4
   5
"""

import sys
input = sys.stdin.readline

def roll_dice(com):
    if com == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = (
            dice[3], dice[1], dice[0], dice[5], dice[4], dice[2])
    elif com == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = (
            dice[2], dice[1], dice[5], dice[0], dice[4], dice[3])
    elif com == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = (
            dice[4], dice[0], dice[2], dice[3], dice[5], dice[1])
    elif com == 4:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = (
            dice[1], dice[5], dice[2], dice[3], dice[0], dice[4])
    return

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]
dv = [(0, 1), (0, -1), (-1, 0), (1, 0)]

for com in command:
    nx, ny = x+dv[com-1][0], y+dv[com-1][1]
    if 0<=nx<n and 0<=ny<m:
        roll_dice(com)
        if board[nx][ny] == 0:
            board[nx][ny] = dice[5]
        else:
            dice[5] = board[nx][ny]
            board[nx][ny] = 0
        print(dice[0])
        x, y = nx, ny
    else:
        continue
