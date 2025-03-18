"""
동생은 고정, 수빈이는 이동

수빈이가 동생 찾는 최단시간 구하기

수빈이 무빙
걷기 : 1초동안 한칸 앞뒤로
순간이동 : 0초 2*x

5 > 10 > 9 > 18 > 17
"""
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

MAX = 100001
visited = [-1] * MAX


def bfs(start, target):
    q = deque([start])
    visited[start] = 0

    while q:
        x = q.popleft()

        if x == target:
            return

        for nx in (2 * x, x - 1, x + 1):
            if 0 <= nx < MAX and visited[nx] == -1:
                if nx == 2 * x:
                    visited[nx] = visited[x]
                    q.appendleft(nx)
                else:
                    visited[nx] = visited[x] + 1
                    q.append(nx)


bfs(n, k)
print(visited[k])