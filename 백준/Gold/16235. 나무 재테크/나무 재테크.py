from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
ground = [[5] * N for _ in range(N)]
tree_map = [[deque() for _ in range(N)] for _ in range(N)]

# 나무 입력 (1-based → 0-based)
for _ in range(M):
    x, y, age = map(int, input().split())
    tree_map[x - 1][y - 1].append(age)

# 8방향 델타
dv = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

for _ in range(K):
    # 봄 & 여름
    dead_map = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if tree_map[i][j]:
                new_deque = deque()
                for age in tree_map[i][j]:
                    if ground[i][j] >= age:
                        ground[i][j] -= age
                        new_deque.append(age + 1)
                    else:
                        dead_map[i][j] += age // 2
                tree_map[i][j] = new_deque

    # 여름: 죽은 나무 처리
    for i in range(N):
        for j in range(N):
            ground[i][j] += dead_map[i][j]

    # 가을: 번식
    for i in range(N):
        for j in range(N):
            for age in tree_map[i][j]:
                if age % 5 == 0:
                    for dx, dy in dv:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < N and 0 <= nj < N:
                            tree_map[ni][nj].appendleft(1)  # 어린 나무를 앞에 추가

    # 겨울: 양분 추가
    for i in range(N):
        for j in range(N):
            ground[i][j] += A[i][j]

# 최종 살아있는 나무 수 세기
ans = 0
for i in range(N):
    for j in range(N):
        ans += len(tree_map[i][j])
print(ans)