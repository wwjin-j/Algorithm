"""
250115
15663 N과 M(9)

line1 N, M 길이, 개수
line2 길이 N 인 수열
output N개의 자연수 중에서 M개를 고른 수열
1 7
1 9
7 1
...
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []
used = [False] * N

def dfs(depth):
    if depth == M:
        print(*ans)
        return

    prev = -1
    for i in range(N):
        if not used[i] and arr[i] != prev:
            used[i] = True
            ans.append(arr[i])
            dfs(depth + 1)
            ans.pop()
            used[i] = False
            prev = arr[i] 

dfs(0)
