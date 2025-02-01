"""
LCS longest common subsequence
"""
import sys
input = sys.stdin.readline

A = [""] + list(input().rstrip())
B = [""] + list(input().rstrip())

array = [['' for _ in range(len(A))] for _ in range(len(B))]

for i in range(1, len(B)) :
    for j in range(1, len(A)) :
        if A[j] == B[i] :
            array[i][j] = array[i-1][j-1] + A[j]
        else :
            if len(array[i][j-1]) > len(array[i-1][j]) :
                array[i][j] = array[i][j-1]
            else :
                array[i][j] = array[i-1][j]

answer = len(array[-1][-1])
print(answer)
if answer != 0 :
    print(array[-1][-1])