"""
250113
16987 계란으로 바위치기

계란에는 내구도와 무게가 있다.
계란 A, B가 있을때 둘이 치게 되면 내구도는 상대 계란의 무게만큼 깎인다.
A(7, 5), B(3, 4) >> A(3, 5), B(-2, 4) 즉, B 계란 깨짐

1. 가장 왼쪽 계란을 든다.
2. 다른 안깨진 다른 계란 중 하나 친다.
3. 손에 든 계란이 깨졌거나 안깨진 계란이 없으면 그냥 넘어간다.
4. 가장 최근에 든 계란을 놓고 그 오른쪽 계란으로 2번 진행한다.
5. 4에서 오른쪽 계란이 없으면 종료한다.

n = 계란에 개수
s, w가 n줄에 걸쳐 들어옴
"""
import sys
input = sys.stdin.readline

n = int(input().strip())
info = [list(map(int, input().split())) for _ in range(n)]
max_broken = 0


def dfs(idx):
    global max_broken

    if idx == n:
        broken_count = 0
        for s, _ in info:
            if s <= 0:
                broken_count += 1
        max_broken = max(max_broken, broken_count)
        return

    if info[idx][0] <= 0:
        dfs(idx + 1)
        return

    any_hit = False
    for target in range(n):
        if target != idx and info[target][0] > 0:
            any_hit = True

            info[idx][0] -= info[target][1]
            info[target][0] -= info[idx][1]

            dfs(idx + 1)

            info[idx][0] += info[target][1]
            info[target][0] += info[idx][1]

    if not any_hit:
        dfs(idx + 1)

dfs(0)
print(max_broken)