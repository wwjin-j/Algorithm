"""
20056 마법사 상어와 파이어볼
"""
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(M)]
for i in range(M):
    info[i][0] -= 1
    info[i][1] -= 1

maps = [[0]*N for _ in range(N)]
directions = [
    (-1, 0), (-1, 1), (0, 1), (1, 1),
    (1, 0), (1, -1), (0, -1), (-1, -1)
]

def move():
    n_map = [[[] for _ in range(N)] for _ in range(N)]
    for r, c, m, s, d in info:
        nr = (r + directions[d][0] * s) % N
        nc = (c + directions[d][1] * s) % N
        n_map[nr][nc].append((m, s, d))
    return n_map

def merge_divide(n_map):
    global info
    info = []

    for r in range(N):
        for c in range(N):
            if not n_map[r][c]:
                continue

            if len(n_map[r][c]) == 1:
                info.append((r, c, *n_map[r][c][0]))
            else:
                total_m = sum(m for m, s, d in n_map[r][c])
                total_s = sum(s for m, s, d in n_map[r][c])
                count = len(n_map[r][c])

                if all(d % 2 == 0 for m, s, d in n_map[r][c]) or all(d % 2 == 1 for m, s, d in n_map[r][c]):
                    n_directions = [0, 2, 4, 6]
                else:
                    n_directions = [1, 3, 5, 7]

                if total_m // 5 > 0:
                    new_m = total_m // 5
                    new_s = total_s // count
                    for d in n_directions:
                        info.append((r, c, new_m, new_s, d))

for _ in range(K):
    n_map = move()
    merge_divide(n_map)

print(sum(m for r, c, m, s, d in info))