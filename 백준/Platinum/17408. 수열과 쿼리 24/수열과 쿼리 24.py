import sys
input = sys.stdin.readline

def merge(a, b):
    return sorted(a + b, reverse=True)[:2]

def build(node, start, end):
    if start == end:
        tree[node] = [arr[start]]
        return
    mid = (start + end) // 2
    build(node * 2, start, mid)
    build(node * 2 + 1, mid + 1, end)
    tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

def update(node, start, end, idx, value):
    if start == end:
        tree[node] = [value]
        return
    mid = (start + end) // 2
    if idx <= mid:
        update(node * 2, start, mid, idx, value)
    else:
        update(node * 2 + 1, mid + 1, end, idx, value)
    tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

def query(node, start, end, left, right):
    if right < start or end < left:
        return []
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    left_res = query(node * 2, start, mid, left, right)
    right_res = query(node * 2 + 1, mid + 1, end, left, right)
    return merge(left_res, right_res)

n = int(input())
arr = list(map(int, input().split()))
tree = [[] for _ in range(4 * n)]

build(1, 0, n - 1)

m = int(input())
for _ in range(m):
    q, a, b = map(int, input().split())
    if q == 1:
        update(1, 0, n - 1, a - 1, b)
    else:
        res = query(1, 0, n - 1, a - 1, b - 1)
        print(res[0] + res[1])