"""
N 개의 마을에 한 명씩 살고있다
M 개의 단방향 도로가 있다
i 번째 길을 지나는데 Ti 만큼 시간 소비한다

파티는 x 번 마을에서 한다.

N, M, X 첫째줄

M 개 줄에 걸쳐 도로의 정보가 주어진다.
도로의 정보 : 시작점, 끝점, Ti 주어진다.
"""

import sys
import heapq

INF = 1e10
input = sys.stdin.readline


def dijkstra(s, edge, n):
    dist = [INF] * (n + 1)
    dist[s] = 0
    q = []
    heapq.heappush(q, (0, s))

    while q:
        d, w = heapq.heappop(q)
        if dist[w] < d:
            continue
        for nxt, c in edge[w]:
            if dist[nxt] > d + c:
                dist[nxt] = d + c
                heapq.heappush(q, (dist[nxt], nxt))
    return dist


n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
reverse_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())

    graph[a].append((b, c))
    reverse_graph[b].append((a, c))

node2x = dijkstra(x, reverse_graph, n)
x2node = dijkstra(x, graph, n)

print(max([x2node[i] + node2x[i] for i in range(1, n + 1) if i != x]))

