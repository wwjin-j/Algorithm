"""
250116
12015 가장 긴 증가하는 부분 수열 2

import sys
n = int(sys.stdin.readline().strip())
li = list(map(int, input().split()))

dp = [1]*n

for i in range(1, n):
    for j in range(i):
        if li[i]>li[j]:
            dp[i]=max(dp[i], dp[j]+1)
print(max(dp))
"""
import sys
input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int, input().split()))
sub = [arr[0]]

def binary(target):
    start, end = 0, len(sub)-1
    while start<=end:
        mid = (start+end)//2
        if sub[mid]==target:
            return mid
        elif sub[mid]<target:
            start = mid+1
        else:
            end = mid-1
    return start

for i in range(N):
    if arr[i]>sub[-1]:
        sub.append(arr[i])
    else:
        tmp = binary(arr[i])
        sub[tmp] = arr[i]

print(len(sub))
#print(sub)
