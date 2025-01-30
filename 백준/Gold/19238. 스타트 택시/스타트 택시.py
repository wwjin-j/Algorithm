"""
스타트 택시
M 명의 승객을 태우는게 목표
활동영역은 N*N
비어있거나 벽
상하좌우 인접 빈칸 이동 가능

최단거리에 있는 승객 태우고
최단거리가 같으면 row 낮은 순서

한칸에 연료 1 소모, 목적지 이동시키면 소모연료 두배 충전

입력
N, M 맵 크기, 목표손님 수
N*N 맵 입력
택시 출발위치 col, row
M 줄에 걸쳐 출발지 col, row, 목적지 col, row

출력
모든손님 이동시킬 수 있으면 남은연료 출력
실패 시 -1

필요함수
1. bfs 거리탐색
2. 승객선정
3. 운행 시뮬레이션
"""
import sys
from collections import deque

input = sys.stdin.readline

# 입력 처리
N, M, fuel = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
ta, xi = map(int, input().split())
ta -= 1
xi -= 1

info = deque()
for _ in range(M):
    q, w, e, r = map(int, input().split())
    info.append((q-1, w-1, e-1, r-1))

# BFS 최단 거리 탐색
def bfs(row, col):
    dv = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque([(row, col)])
    visited = [[-1] * N for _ in range(N)]
    visited[row][col] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in dv:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1 and maps[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    return visited

# 승객 선택 함수
def passenger(visited):
    available_passengers = [t for t in info if visited[t[0]][t[1]] != -1]

    if not available_passengers:
        return None

    # 거리 -> row 순 정렬
    available_passengers.sort(key=lambda t: (visited[t[0]][t[1]], t[0], t[1]))

    chosen_passenger = available_passengers[0]
    info.remove(chosen_passenger)

    return chosen_passenger

# 운행 시뮬레이션
def simulation():
    global fuel, ta, xi

    while info:
        # 현재 위치에서 탐색시작
        d_map = bfs(ta, xi)
        chosen = passenger(d_map)

        if chosen is None:
            return -1

        a, b, c, d = chosen
        distance_1 = d_map[a][b]

        if distance_1 == -1 or fuel < distance_1:
            return -1

        fuel -= distance_1
        ta, xi = a, b

        d_map = bfs(ta, xi)
        distance_2 = d_map[c][d]

        if distance_2 == -1 or fuel < distance_2:
            return -1

        fuel -= distance_2
        fuel += (2 * distance_2)
        ta, xi = c, d

    return fuel

print(simulation())