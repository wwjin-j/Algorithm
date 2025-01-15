"""
구간 합 구하기
N*N 테이블에서 (x1, x2) 부터 (y1, y2)까지의 합
n, m 테이블 사이즈, 테스트케이스
n줄에 걸쳐 테이블 입력
m줄에 걸쳐 테스트 케이스 입력
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(N)]

command = [list(map(int, input().split())) for _ in range(M)]

dp = [[0] * (N+1) for _ in range (N+1)]

for i in range(N):
    for j in range(N):
        dp[i][j] = table[i][j]
        if i > 0:
            dp[i][j] += dp[i-1][j]
        if j > 0:
            dp[i][j] += dp[i][j-1]
        if i > 0 and j > 0:
            dp[i][j] -= dp[i-1][j-1]

for a, b, c, d in command:
    r1, c1, r2, c2 = a - 1, b - 1, c - 1, d - 1
    ans = dp[r2][c2]-dp[r2][c1-1]-dp[r1-1][c2]+dp[r1-1][c1-1]
    print(ans)