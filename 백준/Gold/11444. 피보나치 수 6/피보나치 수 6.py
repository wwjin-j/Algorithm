MOD = 10**9 + 7

def matrix_mult(A, B):
    return [
        [
            (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
            (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD,
        ],
        [
            (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
            (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD,
        ]
    ]

def matrix_pow(matrix, power):
    result = [[1, 0], [0, 1]]
    base = matrix

    while power:
        if power % 2 == 1: 
            result = matrix_mult(result, base)
        base = matrix_mult(base, base)
        power //= 2

    return result

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    base_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_pow(base_matrix, n - 1)
    return result_matrix[0][0] 

n = int(input().strip())
print(fibonacci(n))