"""
250115
14890 경사로
"""
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

def available(li: list):
    used = [False] * N  # 경사로 설치 여부를 체크
    for i in range(N - 1):
        if li[i] == li[i + 1]:  # 높이가 같은 경우
            continue
        elif abs(li[i] - li[i + 1]) > 1:  # 높이 차이가 1 초과인 경우
            return False
        elif li[i] > li[i + 1]:  # 내리막 경사로
            for x in range(1, L + 1):
                if i + x >= N or li[i + 1] != li[i + x] or used[i + x]:
                    return False
                used[i + x] = True
        elif li[i] < li[i + 1]:  # 오르막 경사로
            for x in range(L):
                if i - x < 0 or li[i] != li[i - x] or used[i - x]:
                    return False
                used[i - x] = True
    return True

for i in range(N):
    if available(maps[i]):
        cnt += 1

for col in range(N):
    if available([maps[row][col] for row in range(N)]):
        cnt += 1

print(cnt)
