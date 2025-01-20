"""
250120
12865 평범한 배낭

N개의 물건이 있다.
 각 물건은 무게 W, 가치 V 를 가진다.

최대 K무게만큼 넣을 수 있고 총합 V만큼 즐길 수 있다.

넣을 수 있는 물건들의 가치의 최댓값 출력

N, K 물건의 개수 N, 버틸 수 있는 무게 K
"""
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [0 for _ in range(K+1)]
for item in arr:
    w,v = item
    for i in range(K,w-1,-1):
        dp[i] = max(dp[i],dp[i-w]+v)
print(dp[-1])