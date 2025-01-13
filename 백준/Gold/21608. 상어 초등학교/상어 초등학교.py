"""
250114
21608 상어초등학교
"""
import sys
input = sys.stdin.readline

n = int(input().strip())
info = [list(map(int, input().split())) for _ in range(n**2)]
map = [[0]*n for _ in range(n)]

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def score(i):
    if i==0:
        return 0
    elif i==1:
        return 1
    elif i==2:
        return 10
    elif i==3:
        return 100
    elif i==4:
        return 1000

for num, l1, l2, l3, l4 in info:
    available = []
    for i in range(n):
        for j in range(n):
            if map[i][j]==0:
                love=0
                empty=0
                for d in range(4):
                    nx, ny = i+dx[d], j+dy[d]
                    if nx<0 or nx>=n or ny<0 or ny>=n:
                        continue
                    if map[nx][ny] in (l1, l2, l3, l4):
                        love+=1
                    if map[nx][ny]==0:
                        empty+=1
                available.append([i, j, love, empty])
    available.sort(key=lambda x: (-x[2], -x[3], x[0], x[1]))
    map[available[0][0]][available[0][1]] = num

total_score = 0
for i in range(n):
    for j in range(n):
        num = map[i][j]
        for student in info:
            if student[0] == num:
                _, l1, l2, l3, l4 = student
                break
        p_score = 0
        for d in range(4): 
            nx, ny = i + dx[d], j + dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if map[nx][ny] in (l1, l2, l3, l4):
                p_score += 1
        total_score += score(p_score)

print(total_score)
