
import sys

def check(row, col, num):
    r_p = (row//3)*3
    c_p = (col//3)*3
    for i in range(9):
        if maps[row][i]==num:
            return False
        if maps[i][col]==num:
            return False
    for i in range(r_p, r_p+3):
        for j in range(c_p, c_p+3):
            if maps[i][j]==num:
                return False
    return True

def dfs(depth):
    if depth == len(empty):
        return True
    row, col = empty[depth]
    for i in range(1, 10):
        if check(row, col, i):
            maps[row][col] = i
            flag = dfs(depth+1)
            if flag:
                return True
            maps[row][col]=0
    return False

maps = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(9)]

empty = []
for i in range(9):
    for j in range(9):
        if maps[i][j]==0:
            empty.append((i, j))

dfs(0)

for row in maps:
    print(''.join(map(str, row)))