"""
250113
11053 가장 긴 증가하는 부분수열
"""
import sys
n = int(sys.stdin.readline().strip())
li = list(map(int, input().split()))

dp = [1]*n

for i in range(1, n):
    for j in range(i):
        if li[i]>li[j]:
            dp[i]=max(dp[i], dp[j]+1)
print(max(dp))
