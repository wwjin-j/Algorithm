import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# DP 테이블 초기화
dp = [[0]*N for _ in range(N)]

# 길이가 2인 경우 먼저 계산
for i in range(N-1):
    dp[i][i+1] = matrix[i][0] * matrix[i+1][0] * matrix[i+1][1]

# 길이가 3 이상인 부분 계산 (L: 부분 행렬의 길이)
for L in range(2, N):
    for i in range(N - L):  # i: 부분 행렬의 시작 인덱스
        j = i + L  # j: 부분 행렬의 끝 인덱스
        dp[i][j] = float('inf')  # 초기값을 무한대로 설정

        for k in range(i, j):  # i에서 j 사이에 k를 놓고 최소 곱셈 연산 찾기
            cost = dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1]
            dp[i][j] = min(dp[i][j], cost)

# 결과 출력
print(dp[0][N-1])