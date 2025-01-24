"""
이진검색 트리
"""

import sys
sys.setrecursionlimit(10**5+1)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

def dfs(n):
    for i in graph[n]:
        if not visited[i]:
            visited[i] = n
            dfs(i)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1] = 1
dfs(1)

for k in visited[2:]:
    print(k)