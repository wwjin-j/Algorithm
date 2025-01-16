"""
250116
13397
구간 나누기 2

M개의 구간으로 나누고, 구간 중 최대합을 최소화
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))


def can_divide(arr, max_score, m):
    count, current_min, current_max = 1, arr[0], arr[0]

    for num in arr[1:]:
        current_min = min(current_min, num)
        current_max = max(current_max, num)

        if current_max - current_min > max_score:
            count += 1
            current_min = num
            current_max = num

    return count <= m

def binary_search(arr, m):
    low, high = 0, max(arr) - min(arr)

    while low < high:
        mid = (low + high) // 2
        if can_divide(arr, mid, m):
            high = mid
        else:
            low = mid + 1

    return low

print(binary_search(arr, m))