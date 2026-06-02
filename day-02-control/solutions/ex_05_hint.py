"""Hints for ex_05

    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]

    # Result is 2x2
    C = [[0, 0], [0, 0]]  # or: [[0 for _ in range(2)] for _ in range(2)]

    for i in range(2):        # rows of A
        for j in range(2):    # cols of B
            for k in range(2):  # inner dimension
                C[i][j] += A[i][k] * B[k][j]

    print(C)

    # General case: use len() to get dimensions dynamically
"""
