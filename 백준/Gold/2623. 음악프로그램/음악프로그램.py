"""
2623 음악프로그램

순서 정하기

각각의 보조 pd들이 가져온 순서를 모두 만족하는 전체 공연 순서 출력

"""
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]  # 그래프 초기화 (1-based)
indegree = [0] * (n + 1)  # 진입 차수

# 입력 받기
for _ in range(m):
    data = list(map(int, input().split()))
    for i in range(1, data[0]):
        a = data[i]
        b = data[i + 1]
        graph[a].append(b)    # a → b 순서로 가야 함
        indegree[b] += 1      # b의 진입 차수 증가

# 위상 정렬 시작
queue = deque()
result = []

# 진입 차수 0인 노드부터 시작
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    result.append(now)
    for nxt in graph[now]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)

# 만약 모든 노드를 정렬하지 못했다면 → 사이클 존재
if len(result) != n:
    print(0)
else:
    for i in result:
        print(i)